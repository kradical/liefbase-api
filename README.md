# API

## Setup

* Clone project
  * `$ git clone git@gitlab.com:Liefbase/api.git`
* Create and activate a virtual environment
  * `$ pip3 install virtualenv`
  * `$ python3 -m virtualenv venv` or whatever name you want instead of venv.
  * `$ source venv/bin/activate`
* Install python dependencies
  * `$ pip3 install -r requirements.txt`
* Install [GeoDjango Libraries](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install)
  * `$ sudo apt-get install binutils libproj-dev gdal-bin`
* Install postgresql
  * `$ sudo apt-get install postgresql`
  * `$ sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable`
  * `$ sudo apt-get update`
  * `$ sudo apt-get install postgis`
* Create project database
  * `$ sudo -i -u postgres`
  * `$ psql`
  * `postgres=# create database <database_name>;`
  * `postgres=# \connect <database_name>;`
  * `<database_name>=# create extension postgis;`
* Create development user
  * `<database_name>=# create user <username> password <password> with superuser;`
* Create secret_settings.py under /liefbase, example below
    ```python
    SECRET_KEY = '<secret_key>'  

    DATABASES = {  
        'default': {  
            'ENGINE': 'django.contrib.gis.db.backends.postgis',  
            'NAME': '<database_name>',  
            'USER': '<username>',  
            'PASSWORD': '<password>',  
            'HOST': 'localhost',  
            'PORT': '',  
        }  
    }  

    DEBUG = True
    ```

* Populate initial data
  * `$ python3 manage.py populate`
* Run the server
  * `$ python manage.py runserver`
