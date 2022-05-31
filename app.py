from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.it_college
dept = db.dept

img_path = "../static/images/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electronics')
def electronics():
    data = dept.find_one({ 'name': "school of electronics engineering" })
    after_graduation = img_path + data['images']['after_graduation']
    
    grade_21 = img_path + data['images']['grade_21']
    grade_20 = img_path + data['images']['grade_20']
    grade_19 = img_path + data['images']['grade_19']
    
    return render_template('electronics.html', data=data, after_graduation=after_graduation, grade_21=grade_21,
                           grade_20=grade_20, grade_19=grade_19)

@app.route('/computer')
def computer():
    data = dept.find_one({ 'name': "school of computer science and engineering" })
    after_graduation = img_path + data['images']['after_graduation']
    
    grade_21 = img_path + data['images']['grade_21']
    grade_20 = img_path + data['images']['grade_20']
    grade_19 = img_path + data['images']['grade_19']
    return render_template('computer.html', data=data, after_graduation=after_graduation, grade_21=grade_21,
                           grade_20=grade_20, grade_19=grade_19)

@app.route('/electric')
def electric():
    data = dept.find_one({ 'name': "department of electrical engineering" })
    after_graduation = img_path + data['images']['after_graduation']
    
    grade_21 = img_path + data['images']['grade_21']
    grade_20 = img_path + data['images']['grade_20']
    grade_19 = img_path + data['images']['grade_19']
    return render_template('electric.html', data=data, after_graduation=after_graduation, grade_21=grade_21,
                           grade_20=grade_20, grade_19=grade_19)

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

if __name__ == '__main__':
    app.run(debug=True)

