import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/computer')
def computer():

    return render_template('computer.html')

@app.route('/electric')
def electric():
    return render_template('electric.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.run(debug=True)
