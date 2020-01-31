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


## Manage Project

| Task   | Command  |
|-----------|-----------|
|  Create a new app |    `python manage.py startapp appName`    |
|  Consolidate static files |    `python manage.py collectstatic`    |

## Manage Database

| Task   | Command  |
|-----------|-----------|
|  Migrate the database |    `python manage.py migrate`    |
|  Make migrations |    `python manage.py makemigrations`    |
|  . |    .    |

#### Creating a model
1. Create the model (class) in models.py
2. Add the app to the settings
3. Create a migration
4. Migrate
5. Add the model to the admin

## Manage Users

| Task   | Command  |
|-----------|-----------|
|  Create superuser |    `python manage.py createsuperuser`    |
|  . |    .    |
|  . |    .    |

## Using psql (Postgres)
| Task   | Command  |
|-----------|-----------|
|  Start the service |    `sudo service postgresql start`    |
|  Connect to postgres |    `sudo -u postgres psql`    |
|  Quit psql |    `\q`    |
|  Check user accounts |    `\du`    |
|  Create database |    `CREATE DATABASE name;`    |
|  Check port number |    `\conninfo`    |
|  Change user password |    `\password username`    |
|  Delete Database |    `DROP DATABASE db_name`    |
|  . |    .    |