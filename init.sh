#!/bin/bash

echo "update & upgrade packages"
sudo apt -y update && sudo apt -y upgrade

echo "install Python"
sudo apt install -y python3

echo "install pip"
sudo apt install -y python3-pip

echo "install MongoDB"
sudo apt install -y mongodb

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
