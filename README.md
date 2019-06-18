# Django Start Project

A boilerplate to a start django 2 project.

## Installation

Install the dependencies start the server.


```code
$ git clone https://github.com/marlonleite/django_start_project.git

$ mv .env_exemple .env

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install --upgrade pip

$ pip install -r requirements.txt
```


## Optional Config

Edit the file .env:

```code
SECRET_KEY=CHANGE_ME_HERE
DEBUG=True
ALLOWED_HOSTS=*

PROJECT_TITLE=CHANGE_ME_HERE
PROJECT_AUTHOR=CHANGE_ME_HERE
PROJECT_AUTHOR_URL=CHANGE_ME_HERE
GOOGLE_KEY_MAPS=CHANGE_ME_HERE

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=25
EMAIL_USE_TLS=False
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## Create User and Run project
Migrate db:
```code
./manage.py migrate
```

Create superuser:
```code
./manage.py createsuperuser
```

Run:
```code
./manage.py runserver
```
## Start Theme

- https://github.com/BlackrockDigital/startbootstrap-creative
- https://github.com/BlackrockDigital/startbootstrap-sb-admin-2
