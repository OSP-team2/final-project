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
    url = u'https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317400'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    computer_intro = soup.select('.bg_gr')[0].text
    computer_prop = soup.select('.bx1_wh')[2].text
    computer_job = soup.select('.bx1_wh')[4].text
    
    return render_template('computer.html', intro=computer_intro, prop=computer_prop, job=computer_job)

@app.route('/electric')
def electric():
    url = u'https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317404'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    electric_intro = soup.select('.bg_gr')[0].text
    electric_prop = soup.select('.bx1_wh')[2].text
    electric_job = soup.select('.bx1_wh')[4].text
    return render_template('electric.html', intro=electric_intro, prop=electric_prop, job=electric_job)

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.run(debug=True)
