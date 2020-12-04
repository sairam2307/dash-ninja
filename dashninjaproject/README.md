# Steps to follow

# Clone the project
1. git clone https://github.com/sairam2307/dash-ninja.git

# Download Python
2. Download Python 3.5.2 from https://www.python.org/downloads/release/python-352/

# Install virtualenv
2.  pip install virtualenv

# Create virtualenv using Python
3. virtualenv  myenv

# Activate virtualenv.
4.  myenv/Script/activate

# Go to manage.py file located directory and install requirements - 
5. pip install -r requirements.txt

# Migrate the app
6. python manage.py migrate

# Run the server
7. python manage.py runserver

# Create superuser as admin to login
8. python manage.py createsuperuser(Enter username and password to login)

# Login to admin to create, update , delete for category, items, footer and company 
11. http://127.0.0.1:8000/admin (Enter username and password)

# After creating or updating models or database go to the homepage by using below url
12. http://127.0.0.1:8000
