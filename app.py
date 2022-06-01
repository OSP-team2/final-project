from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from pymongo import MongoClient

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    grade = SelectField('연도 선택:', choices=[('grade_21', '2021학년도'), ('grade_20', '2020학년도'), ('grade_19', '2019학년도')])
    submit = SubmitField('Submit')

client = MongoClient()
db = client.it_college
dept = db.dept

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electronics', methods=['GET', 'POST'])
def electronics():
    form = InfoForm()
    path = "grade_21"
    
    if form.validate_on_submit():
        path = form.grade.data
    
    data = dept.find_one({ 'name_ko': "전자공학부" })
    
    return render_template('electronics.html', form=form, path=path, data=data)

@app.route('/computer', methods=['GET', 'POST'])
def computer():
    form = InfoForm()
    path = "grade_21"
    
    if form.validate_on_submit():
        path = form.grade.data
        
    data = dept.find_one({ 'name_ko': "컴퓨터학부" })
    
    return render_template('computer.html', form=form, path=path, data=data)

@app.route('/electric', methods=['GET', 'POST'])
def electric():
    form = InfoForm()
    path = "grade_21"
    
    if form.validate_on_submit():
        path = form.grade.data
        
    data = dept.find_one({ 'name_ko': "전기공학과" })
    
    return render_template('electric.html', form=form, path=path, data=data)

if __name__ == '__main__':
    app.run(debug=True)

