import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.it_college
dept = db.dept

dept.drop()



dept_urls = ["https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317397", "https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317400",
        "https://home.knu.ac.kr/HOME/it/sub.htm?nav_code=it1623317404"]

intros = []
props = []
jobs = []

for url in dept_urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    intros.append(soup.select('.bg_gr')[0].text)
    props.append(soup.select('.bx1_wh')[2].text)
    jobs.append(soup.select('.bx1_wh')[4].text)
    
corp_urls = ["https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=UjVaSHBEcTFsdFUzQ3F4dDFTeXVKZz09",
            "https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=NThFa2lRajFWNFhkcTFuNlRLSExXUT09",
            "https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=RS9DMFhmN3g1R09ZTTA3aEw3SmtNUT09",
            "https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=eHFqTEhJeHB6SDRFUkQ3RVl0dGlyQT09",
            "https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=MVdTK1FaMUZSUGVDaXVpUUgrb29PZz09",
            "https://www.saramin.co.kr/zf_user/company-info/view-inner-salary?csn=SjNOeE1FK2NkTnFvM0wvYzhwNU4vZz09"]

corps = []
pays = []

for url in corp_urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    corps.append(soup.select('.name')[0].text)
    pays.append(soup.select('.average_currency')[0].text)

electronics_doc = {
    'name_en': "School of Electronics Engineering",
    'name_ko': "전자공학부",
    'location': "IT1호관 409호",
    'number': '053-950-5506',
    'introduction': intros[0],
    'property': props[0],
    'job': jobs[0],
    'corporation_name' : [ corps[0], corps[1] ],
    'corporation_pay' : [ pays[0], pays[1] ],
    'images': {
        'after_graduation': 'electronics.jpg',
        'location': 'electronics_loc.jpg',
        'wage': 'electronics_wage.jpg',
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
    'corporation_name' : [ corps[2], corps[3] ],
    'corporation_pay' : [ pays[2], pays[3] ],
    'images': {
        'after_graduation': 'computer.jpg',
        'location': 'computer_loc.jpg',
        'wage': 'computer_wage.jpg',
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
    'corporation_name' : [ corps[4], corps[5] ],
    'corporation_pay' : [ pays[4], pays[5] ],
    'images': {
        'after_graduation': 'electric.jpg',
        'location': 'electric_loc.jpg',
        'wage': 'electric_wage.jpg',
        'grade_21': 'electric_grade_21.jpg',
        'grade_20': 'electric_grade_20.jpg',
        'grade_19': 'electric_grade_19.jpg'
    }
}

dept.insert_many([electronics_doc, computer_doc, electric_doc])

