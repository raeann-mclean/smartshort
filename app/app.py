
#flaks tools
#redirect imported not used yet, but will be used to redirect short urls to long urls
#takes python dic and sends json response to client
#render_template used to render html templates
from flask import Flask, redirect, request, jsonify, render_template
import string
import random

app = Flask(__name__)

# dic is "database" for storing short code and long url pairs 
# NOT REAL DATABASE YET. links will obv be lost on server restart

url_map = {}  #dictionary 4 storing

@app.route("/") #cute lil home page
def home():
    return render_template('home.html')

#generate rand 6 digit short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



@app.route('/shorten', methods=['POST']) #main feature
def shorten():

    data = request.get_json() #get json data from request body
    long_url = data.get('url') #get long url from json data

    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400
    
    code = generate_code() #call func to gen short code
    url_map[code] = long_url #store short code & long url in dic
    return jsonify({'short_url': f'http://localhost:5000/{code}'}) #route doesn't exist yet but will be created to handle redirection

@app.route('/<code>')
def redirect_long(code):
    long_url = url_map.get(code)
    if not long_url:
        return jsonify({'error' : 'cant find short code :('}), 404
    return redirect(long_url)

@app.route('/links', methods=['GET']) #see all short code and long url pairs in dic
def links():
    return jsonify(url_map)


if __name__ == '__main__':
    app.run(debug=True)