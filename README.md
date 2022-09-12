# nindobackend

## What the applicaion is doing:

This Django application is a POC which could in some way represent the backend of nindo.de
The main data structure is inspired by https://github.com/merlinfuchs/nindo.de

The approach which was used is based on Django, since Django allows you to work with Database-Tables (Models) the same way you work with classes.
It also comes with a variety of Plugins (for this demo a GraphQL-Plugin was used and an according Endpoint was configured - see below)

### The main files:
- The models.py file is defining the database tables and their relationships.
- The admin.py file is defining the admin interface for the database tables. (localhost:8000/admin)
- The schema.py file is defining the GraphQL schema. (localhost:8000/graphql)


## Setup
prepare your venv from requirements.txt:
```
pip install -r requirements.txt
```
create the database:
```
python manage.py makemigrations
python manage.py migrate
```
create the admin user:
```
python manage.py createsuperuser
```
load fixtures from dummydata.json
```
python manage.py loaddata dummydata.json
```
run the test server:
```
python manage.py runserver 0.0.0.0:8000
```

## Usage Django Admin
In this demo you can access the Django-Admin-Interface like so:
```
http://localhost:8000/admin/
```
Login with the superuser you just created
You can navigate through the data using the web-page to do rudimentar stuff.


## Usage GraphQL
open the GraphQL interface like so:
```
http://localhost:8000/graphql/
```
Run some Queries (Hit CTRL+SPACE to see suggestions)

![image](https://user-images.githubusercontent.com/52819910/189770786-0e28faf8-7a34-4842-b376-ad439218bd38.png)


Additional Documentation:
https://docs.graphene-python.org/projects/django/en/latest/
https://docs.djangoproject.com/en/3.2/
