# Simple inventory Application

# Project Overview 
The goal is to design and create the structure of an inventory app which would allow a store to keep of its inventory of products via API. 

# Features

# Screenshots

# Requirements
Version >=  of 3.9.10 `PYTHON` requires Django Rest framework 3.13.1 or above (previous versions should support Django all the way back to around 3.1).

# Setup
The first thing to do is to clone the repository:

    $ git clone https://github.com/Sundarmax/inventory-app.git
    $ cd inventory-app

Create a virtual environment to install dependencies in and activate it:

    $ virtualenv2 --no-site-packages env
    $ source env/bin/activate

Then install the dependencies:

    (env)$ pip install -r requirements.txt

Note the  `(env)`  in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by  `virtualenv2`.

Please skip this step if you haven't configured the database locally. 

     (env)$ python manage.py migrate


## Run the project 

Once  `pip`  has finished downloading the dependencies:

    (env)$ python manage.py runserver

And navigate to  `http://127.0.0.1:8000/api/v1/product/list/ 
This is an Open API which will redirect you to browsable API page where you can able to send a message to end user. 


## Test driven development 

Please use the below command to run the unit test file in app.

    (env)$ python manage.py test 

