from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".")

# Главная страница
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# JS файл
@app.route("/app.js")
def js():
    return send_from_directory(".", "app.js")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)