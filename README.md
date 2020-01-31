# Virtual Environment

| Task        | Command       |
| ------------- |--------------|
| Create virtual environment      | `python3 -m venv venv` |
| Activate virtual environment      | `source venv/bin/activate`      |
|  Deactivate virtual environment |    `deactivate`    |
| List installed packages |   `pip list`     |
| Create requirements.txt file  |  `pip freeze > requirements.txt`      |
|  Install packages from requirements.txt |    `pip install -r requirements.txt`    |
|  . |    .    |
|  . |    .    |

# Django

## Start Project
| Task   | Command  |
|-----------|-----------|
|  Creating a new project |    `django-admin startproject project_name`    |
|  Start a server |    `python manage.py runserver`    |
|  . |    .    |
|  . |    .    |


## Build Project

| Task   | Command  |
|-----------|-----------|
|  Create a new app |    `python manage.py startapp appName`    |
|  . |    .    |

## Manage Database

| Task   | Command  |
|-----------|-----------|
|  Migrate the database |    `python manage.py migrate`    |
|  Make migrations |    `python manage.py makemigrations`    |
|  . |    .    |

## Manage Users

| Task   | Command  |
|-----------|-----------|
|  Create superuser |    `python manage.py createsuperuser`    |
|  . |    .    |
|  . |    .    |