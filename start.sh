#!/bin/bash
pip3 install -r requirements.txt --user
python3 image_repo/manage.py makemigrations
python3 image_repo/manage.py migrate
python3 image_repo/manage.py runserver
open -a "Google Chrome" http://127.0.0.1:8000