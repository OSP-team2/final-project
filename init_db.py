import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.it_college
dept = db.dept

dept.drop()

urls = ["https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317397", "https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317400",
        "https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317404"]
intros = []
props = []
jobs = []

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    intros.append(soup.select('.bg_gr')[0].text)
    props.append(soup.select('.bx1_wh')[2].text)
    jobs.append(soup.select('.bx1_wh')[4].text)

electronics_doc = {
    'name_en': "School of Electronics Engineering",
    'name_ko': "전자공학부",
    'location': "IT1호관 409호",
    'number': '053-950-5506',
    'introduction': intros[0],
    'property': props[0],
    'job': jobs[0],
    'images': {
        'after_graduation': 'electronics.jpg',
        'grade_21': 'electronics_grade_21.jpg',
        'grade_20': 'electronics_grade_20.jpg',
        'grade_19': 'electronics_grade_19.jpg'
    }
}

computer_doc = {
    'name_en': "School of Computer Science and Engineering",
    'name_ko': "컴퓨터학부",
    'location': "공대9호관 413호",
    'number': '053-950-5550/6370',
    'introduction': intros[1],
    'property': props[1],
    'job': jobs[1],
    'images': {
        'after_graduation': 'computer.jpg',
        'grade_21': 'computer_grade_21.jpg',
        'grade_20': 'computer_grade_20.jpg',
        'grade_19': 'computer_grade_19.jpg'
    }
}

electric_doc = {
    'name_en': "Department of Electrical Engineering",
    'name_ko': "전기공학과",
    'location': "공대8호관 308호",
    'number': '053-950-5600', 
    'introduction': intros[2],
    'property': props[2],
    'job': jobs[2],
    'images': {
        'after_graduation': 'electric.jpg',
        'grade_21': 'electric_grade_21.jpg',
        'grade_20': 'electric_grade_20.jpg',
        'grade_19': 'electric_grade_19.jpg'
    }
}

dept.insert_many([electronics_doc, computer_doc, electric_doc])

