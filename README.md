# A Django application using AbstractUser class 

## Installation

To install the project on Ubuntu 18.04, follow the instructions:

1) Clone the remote repository:
git clone git@github.com:edyta555/django_users.git

2) Create a virtual environment:
python3 -m venv myvenv

3) Activate the virtual environment:
source myvenv/bin/activate

4) Upgrade pip:
python3 -m pip install --upgrade pip

5) Enter the project folder:
cd django_users

6) Install requirements:
pip install -r requirements.txt

7) Migrate:
python3 manage.py migrate

8) Run the development server:
python3 manage.py runserver

The website should now be available at the address:
http://127.0.0.1:8000/main/users/
