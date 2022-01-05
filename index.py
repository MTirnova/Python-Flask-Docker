from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def hello():
    kullanici = os.getenv("KULLANICIADI","UYARI!Herhangi bir mesaj yok.")
    return "Merhaba, "+ kullanici +" hosgeldiniz."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

