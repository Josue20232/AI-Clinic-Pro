from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "L'API de l'AI Clinic est en marche !"

if __name__ == "__main__":
    app.run()