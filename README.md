
# Offspring Inventory Management System
This is an Inventory Management System built using python for Offspring Company Limited. It is a system that will help track and manage stocks for Offspring Company Limited and provide invoices to their various customers. Additionally, it will help the company analyse sales of their different products using line graphs.

# Authors
Bright Mukonesi
Rewel Kinyanjui
Jaquiline Wangu
George Mwai
Abigail Wambui

# Features
As an administartor, You will be able to:

Sign in with the application to start using.
Record sales.
Track down distributed orders.
Determine sales analysis of a particular product.
Provide customers with an ivoice.
As a user, You will be able to:

View all the above but not change the system.

# Installing


Clone this repo: git clone https://github.com/gichimux/offspring-project.git.

The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
On your terminal,Create database gallery using the command below.

CREATE DATABASE instaclone; 
**if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME
Migrate the database using the command below

python3.6 manage.py migrate
Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver
Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

Running the tests
Use the command given below to run automated tests.

    python manage.py test 

# Built With
Python - language to formulate code
Django - web framework used
HTML - For building Mark Up pages/User Interface
CSS - For Styling User Interface

# License
This project is licensed under the MIT License.Copyright 2019(Offspring IMS)
