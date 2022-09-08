import json
from werkzeug.utils import secure_filename
from random import random
from flask import Flask, render_template, url_for, send_from_directory, request, redirect, jsonify, Response
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/petunjuk')
def petunjuk():
    return render_template('petunjuk.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')
    
@app.route('/<path:resource>')
def serveStaticResource(resource):
	return send_from_directory('static/', resource)

if __name__ == "__main__" :
    app.run(debug=True)