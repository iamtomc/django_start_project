# Django Start Project

A boilerplate to Start Django project

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

Edit the file settings.py:

```code
PROJECT = {
    'title': config('PROJECT_TITLE'),
    'description': "",
    'author': config('PROJECT_AUTHOR'),
    'author_url': config('PROJECT_AUTHOR_URL'),
    'maps': config('GOOGLE_KEY_MAPS'),
}
```

