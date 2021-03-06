# PYTHON (Flask) RESTful API

## Setting up the Flask app

1. You have to install python on your machine (this project uses python version 3.7.9):

    * To install python visit the official python website : [Python official website](https://www.python.org/downloads/)
    * you can verify your python installation by running the following command:
      
      python --version
      
2. You have to create a virtual environement:

    * First, install virtualenv : pip install virtualenv
    * Create your virtual environement : python -m venv venv
    * Active your virtual environement : . ./venv/Scripts/activate
    
3. You have to install the dependencies using pip and requirements.txt file:

    * To install the dependencies run the following command: pip install -r requirements.txt
    
4. You have to create the database schema using the following commands(this project uses SQLite3 as a database):

    * To create the database run: 
        1. python app.py db init
        2. python app.py db migrate
    
5. Finaly, you have to run the server:
    
    * To run the server: flask run
