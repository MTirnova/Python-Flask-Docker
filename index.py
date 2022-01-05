from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def hello():
    message = os.getenv("KULLANICIADI","UYARI!Herhangi bir mesay yok.")
    return "Merhaba, "+message+" hosgeldiniz."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

