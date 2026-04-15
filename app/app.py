
#
from flask import Flask, redirect, request, jsonify, render_template
import string
import random

app = Flask(__name__)

url_map = {}  #dictionary 4 storing

@app.route("/")
def home():
    return render_template('home.html')


def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    long_url = data.get('url')
    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400
    code = generate_code()
    url_map[code] = long_url
    return jsonify({'short_url': f'http://localhost:5000/{code}'})

@app.route('/links', methods=['GET'])
def links():
    return jsonify(url_map)