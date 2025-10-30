from flask import Flask, render_template_string, request

app = Flask(__name__)
app.secret_key = "supersecretkey123"

FIXED_PASSWORD = "freudianslip"

html = """
<!DOCTYPE html>
<html>
<head>
    <title></title> <!-- No tab title -->
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(120deg, #75975e, #658354, #445626);
            font-family: 'Comic Sans MS', cursive, sans-serif;
            overflow: hidden;
        }
        .container {
            text-align: center;
        }
        input[type="text"] {
            font-size: 18px;
            padding: 8px;
            border-radius: 8px;
            border: 2px solid #333;
        }
        .button {
            margin-top: 15px;
            font-size: 20px;
            padding: 10px 25px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            background-color: black;
            color: white;
        }
        .popup {
            background-color: #8fbd95;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(0,0,0,0.3);
            animation: popin 0.5s ease;
        }
        .error {
            color: red;
            font-weight: bold;
            margin-top: 20px;
            font-size: 25px;
            animation: shake 0.3s;
        }
        h1 {
            font-size: 40px;
            color: #FF1493;
            animation: rainbow 3s infinite;
        }
        p.message {
            font-size: 25px;
            color: #FF69B4;
        }

        @keyframes popin {
            0% { transform: scale(0.5); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            50% { transform: translateX(10px); }
            75% { transform: translateX(-10px); }
        }
        @keyframes rainbow {
   	    0% { color: #FFB6C1; }   /* Light Pink */
    	    25% { color: #FF69B4; }  /* Hot Pink */
    	    50% { color: #7CFC00; }  /* Lawn Green (her favorite) */
    	    75% { color: #DA70D6; }  /* Orchid */
    	    100% { color: #FFC0CB; } /* Pink */

        }

        .emoji {
            font-size: 50px;
            animation: bounce 1s infinite alternate;
        }

        @keyframes bounce {
            0% { transform: translateY(0); }
            100% { transform: translateY(-20px); }
        }

        .heart {
            position: absolute;
            font-size: 30px;
            animation: float 4s infinite;
        }
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); }
            100% { transform: translateY(-500px) rotate(360deg); }
        }

    </style>
</head>
<body>
<div class="container">
    {% if not success %}
        <div class="popup">
            <form method="POST">
                <p>Enter the secret password:</p>
                <input type="text" name="password" required>
                <br>
                <button type="submit" class="button">Submit</button>
            </form>
            {% if error %}
                <div class="error">Password Incorrect! ❌</div>
            {% endif %}
        </div>
    {% else %}
        <div class="popup">
            <h1>Hey ___! 💖</h1>
            <p class="message">You always make my day a little better.</p>
            <p class="message">Okay thats it bye! 🤍</p>
	    <p class="emoji">☺️😊🙂</p>
        </div>
        <!-- Floating hearts -->
        <div class="heart" style="left:10%;">❤️</div>
        <div class="heart" style="left:50%;">💖</div>
        <div class="heart" style="left:80%;">💗</div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    error = False
    success = False

    if request.method == "POST":
        password = request.form.get("password")
        if password == FIXED_PASSWORD:
            success = True
        else:
            error = True

    return render_template_string(html, error=error, success=success)


if __name__ == "__main__":
    app.run(debug=True)
