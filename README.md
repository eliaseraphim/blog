# Personal Blog

## Description

Personal blog created with Django. Simple project for fun.

## Developer

| Name       | Email                 |
|:-----------|:----------------------|
| Elia Deppe | elia.deppe7@gmail.com |

## Documentation

Online Documentation is available here: https://eliaseraphim.github.io/blog/

## Requirements

### Python

- 3.8.x
- 3.9.x
- 3.10.x

### Packages

| Package              | Version  | PyPI                                           | Documentation                                          | Repository                                       | Purpose              | Required |
|:---------------------|:---------|:-----------------------------------------------|:-------------------------------------------------------|:-------------------------------------------------|:---------------------|:---------|
| Django               | 4.1.5    | https://pypi.org/project/Django/               | https://docs.djangoproject.com/en/4.1/                 | https://github.com/django/django                 | Backend Software     | Yes      |
| Pillow               | 9.4.0    | https://pypi.org/project/Pillow/               | https://pillow.readthedocs.io/en/stable/               | https://pypi.org/project/Pillow/                 | Image Processing     | Yes      |
| django-cleanup       | 6.0.0    | https://pypi.org/project/django-cleanup/       | See: PyPI or Repository                                | https://github.com/un1t/django-cleanup           | Backend Software     | Yes      |
| django-debug-toolbar | 3.8.1    | https://pypi.org/project/django-debug-toolbar/ | https://django-debug-toolbar.readthedocs.io/en/latest/ | https://github.com/jazzband/django-debug-toolbar | Debug Tool           | No       |
| sphinx               | 6.1.3    | https://pypi.org/project/Sphinx/               | https://www.sphinx-doc.org/en/master/                  | https://github.com/sphinx-doc/sphinx             | Documentation Engine | No       |
| sphinx-rtd-theme     | 1.2.0rc2 | https://pypi.org/project/sphinx-rtd-theme/     | https://sphinx-rtd-theme.readthedocs.io/en/stable/     | https://github.com/readthedocs/sphinx_rtd_theme  | Documentation Theme  | No       |

## Installation

It is recommended that you create a virtual environement, though not necessary. Learn more about virtual environments, 
and how to use them here: https://realpython.com/python-virtual-environments-a-primer/

```commandline
git clone https://github.com/eliaseraphim/blog.git
mkvirtualenv blog [-a PATH/TO/blog]
workon blog
pip install -r requirements.txt
cd core
python manage.py makemigrations
python manage.py migrate
```

## Run

```commandline
workon blog
cd core
python manage.py runserver 8000
```

## Build Documentation

Documentation is built in the `/core/docs`. The `/docs` folder in root is for published documentation.

```commandline
workon blog
cd core/docs/
make html
```
