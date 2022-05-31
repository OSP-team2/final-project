#!/bin/bash

echo "create venv"
python3 -m venv .venv

echo "activate venv"
source .venv/bin/activate

echo "install packages"
pip install -r requirements.txt

echo "set up database"
python init_db.py

echo "run flask"
flask run --host=0.0.0.0
