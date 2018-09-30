# Genomics England Project

This repo is a Rest API application in python having 2 end points
- GET method that returns the timestamp
- POST method that performs calculation (sum, substract, divide, product) between 2 numbers.

The API can be requested by using POSTMAN (or curl). Moreover, a quick web interface has been developed.

### Getting started
```
pip install -r requirements.txt
python appserver.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) 

### Application structure

__appserver.py__: start-up script for running the app application.

__requirements.txt__: lists the package dependencies so that it is easy to regenerate an
identical virtual environment on a different computer.

__venv/__ : virtual env folder necessary to create isolated Python environments.

- __app/__

    - __\_\_init\_\_.py__: turns the app directory into a valid Python package
    - __api.py__: for defining REST API route endpoints capable of consuming and producing JSON request and responses
    - __application.py__: for creating an instance of the Flask application
    - __config.py__: contains configuration settings for the Flask application
    - __forms.py__: module to store web form classes
    - *__static/__*: The static directory contains the static files of the project like CSS, JS, images files necessary for the views.
    - *__templates/__*: The templates directory contains templates like HTML files necessary to generate views.
    - __tests/__: this folder contains my unit tests
    
### Tests
Standalone unit tests run with:

```python -m unittest discover```

### Author
GILLES Annthomy
