
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hi hi! Lets experiment with making a link shortener w/ flask + use docker for ease of use + SQLite for storage. This is the home page. Try going to /shorten to shorten a link or /links to see all shortened links."