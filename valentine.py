from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>My Valentine ❤️</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            width: 360px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        .names {
            font-size: 18px;
            color: #ff4d6d;
            margin-bottom: 10px;
            font-weight: bold;
        }

        img {
            width: 220px;
            height: 220px;
            object-fit: cover;
            border-radius: 50%;
            border: 5px solid #ff4d6d;
            margin-bottom: 15px;
        }

        h1 {
            color: #ff4d6d;
            font-size: 22px;
        }

        .buttons {
            margin-top: 20px;
            position: relative;
            height: 60px;
        }

        button {
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
        }

        #yes {
            background: #ff4d6d;
            color: white;
        }

        #no {
            background: #ccc;
            position: absolute;
        }

        .final {
            display: none;
            font-size: 22px;
            color: #ff4d6d;
            margin-top: 20px;
        }
    </style>
</head>

<body>

<div class="card">

    <!-- ❤️ CHANGE NAMES HERE ❤️ -->
    <div class="names">
        Kulsumma ❤️ Thakkudu
    </div>

    <img src="/static/couple.png">

    <h1 id="question"></h1>

    <div class="buttons">
        <button id="yes" onclick="nextQuestion()">YES 💖</button>
        <button id="no" onmouseover="moveNo()">NO 💔</button>
    </div>

    <div class="final" id="finalMessage">
        I love you forever ❤️🥰
    </div>
</div>

<!-- 🎵 MUSIC (starts after YES) -->
<audio id="music" loop>
    <source src="/static/music.mp3" type="audio/mpeg">
</audio>

<script>
    // ❤️ QUESTIONS ❤️
    const questions = [
        "Will you be my Valentine? 💘",
        "Do you promise to stay with me always? 🥰",
        "Will you hold my hand through everything? 🤝",
        "Will you be mine forever? 💍"
    ];

    let index = 0;
    let musicStarted = false;

    document.getElementById("question").innerText = questions[index];

    function nextQuestion() {
        if (!musicStarted) {
            document.getElementById("music").play();
            musicStarted = true;
        }

        index++;

        if (index < questions.length) {
            document.getElementById("question").innerText = questions[index];
        } else {
            document.querySelector(".buttons").style.display = "none";
            document.getElementById("question").style.display = "none";
            document.getElementById("finalMessage").style.display = "block";

            setTimeout(openWhatsApp, 2000);
        }
    }

    function moveNo() {
        let x = Math.random() * 200 - 100;
        let y = Math.random() * 80 - 40;
        document.getElementById("no").style.transform =
            `translate(${x}px, ${y}px)`;
    }

    function openWhatsApp() {
        // 🔴 CHANGE THESE 🔴
        let phone = "917594919605"; // countrycode + number
        let message = "I said YES ❤️🥰 I love you forever!";
        let url = "https://wa.me/" + phone + "?text=" + encodeURIComponent(message);
        window.open(url, "_blank");
    }
</script>

</body>
</html>
""")

if __name__ == "__main__":
    # ✅ REQUIRED FOR RENDER
    app.run(host="0.0.0.0", port=10000)
