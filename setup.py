#!/usr/bin/env python3
import shutil
import os

#make sure working directory is the same as the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create a virtual environment
shutil.rmtree('env', ignore_errors=True)
os.system('python3 -m venv env')

#upgrade pip
os.system('env/bin/pip install --upgrade pip')

# install the requirements from requirements.txt
os.system('env/bin/pip install -r requirements.txt')




