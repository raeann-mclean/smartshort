
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hi hi! Lets experiment with making/using a DevOps pipeline!"