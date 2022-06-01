# I-Teen

## Description
대학 입시생 및 신입생들을 위한 경북대학교 IT대학 소개 웹사이트입니다.

## Environment
Python 3.8.10

MongoDB v3.6.8

## Quick Start
1. 저장소를 클론해서 로컬 환경에 가져옵니다.
   1. HTTPS
      ```bash
      git clone https://github.com/OSP-team2/final-project.git
      ```
   2. SSH
      ```bash
      git clone git@github.com:OSP-team2/final-project.git
      ```

2. final-project 폴더로 이동 후 init.sh를 실행합니다.
   ```bash
   ./init.sh
   ```

## Steb-by-step Start
1. 저장소를 클론해서 로컬 환경에 가져옵니다.
   1. HTTPS
      ```bash
      git clone https://github.com/OSP-team2/final-project.git
      ```
   2. SSH
      ```bash
      git clone git@github.com:OSP-team2/final-project.git
      ```

2. final-project 폴더로 이동 후 Python 가상환경을 만듭니다.
   ```bash
   python3 -m venv .venv
   ```

3. 가상환경을 실행합니다.
   ```bash
   source .venv/bin/activate
   ```

4. requirements.txt에 적혀있는 패키지들을 설치합니다.
   ```bash
   pip install –r requirements.txt
   ```

5. init_db.py를 실행하여 기본 데이터베이스를 구축합니다.
   ```bash
   python init_db.py
   ```

6. Flask를 실행합니다.
   ```bash
   flask run --host=0.0.0.0
   ```
