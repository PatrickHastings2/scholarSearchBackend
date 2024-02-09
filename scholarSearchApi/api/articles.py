from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Setup of key Flask object (app)
app = Flask(__name__)
# Setup SQLAlchemy object and properties for the database (db)
database = 'sqlite:///sqlite.db'  # path and filename of database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy()

# This belongs in place where it runs once per project
db.init_app(app)

""" database dependencies to support sqlite examples """
import datetime
from datetime import datetime
import json


from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into a Python shell and follow along '''


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Article(db.Model):
   __tablename__ = 'articles'  # table name is plural, class name is singular


   # Define the User schema with "vars" from object
   id = db.Column(db.Integer, primary_key=True)
   _title = db.Column(db.String(255), unique=False, nullable=False)
   _author = db.Column(db.String(255), unique=True, nullable=False)
   _link = db.Column(db.String(255), unique=True, nullable=False)


# constructor of a Article object, initializes the instance variables within object (article)
def __init__(article, title, author, link):
    article._title = title   
    article._author = author
    article._link = link


   # CRUD create/add a new record to the table
   # returns article or None on error
def create(article):
       try:
        # creates an article object from Article(db.Model) class, passes initializers
        db.session.add(article)  # add prepares to persist person object to Users table
        db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
        return article
       except IntegrityError:
           db.session.remove()
           return None


   # CRUD read converts self to dictionary
   # returns dictionary
def read(article):
    return {
           "id": article.id,
           "title": article.title,
           "author": article.author,
           "link": article.link,
       }


# CRUD delete: remove article
# None
def delete(article):
    db.session.delete(article)
    db.session.commit()
    return None
  
# Database Creation and Testing


# Builds working data for testing

def initArticles():
    with app.app_context():
        db.create_all()
        u1 = Article(title='12 Strategies to Writing the Perfect College Essay', author='Pamela Reynolds', link='https://summer.harvard.edu/blog/12-strategies-to-writing-the-perfect-college-essay/')
        u2 = Article(title='Nikola Tesla', author='niko', link='123niko')
        u3 = Article(title='Alexander Graham Bell', uid='lex', link='123lex')
        u4 = Article(title='Eli Whitney', author='whit', link='123whit')
        u5 = Article(title='Indiana Jones', author='indi', link='')
        u6 = Article(title='Marion Ravenwood', author='raven', link='')

    articles = [u1, u2, u3, u4, u5, u6]


"""Builds sample user/note(s) data"""
for article in articles:
    try:
        '''add article to table'''
        object = article.create()
        print(f"Created new uid {object.uid}")
    except:  # error raised if object nit created
        '''fails with bad or duplicate data'''
        print(f"Records exist uid {article.uid}, or error.")
              
initUsers()


# SQLAlchemy extracts single user from database matching User ID
def find_by_uid(uid):
   with app.app_context():
       user = User.query.filter_by(_uid=uid).first()
   return user # returns user object


# Check credentials by finding user and verify password
def check_credentials(uid, password):

# query email and return user record
   user = find_by_uid(uid)
   if user == None:
       return False
   if (user.is_password(password)):
       return True
   return False
      
#check_credentials("indi", "123qwerty")


# Inputs, Try/Except, and SQLAlchemy work together to build a valid database object
def create():
   # optimize user time to see if uid exists
   uid = input("Enter your user id:")
   user = find_by_uid(uid)
   try:
       print("Found\n", user.read())
       return
   except:
       pass # keep going
  
   # request value that ensure creating valid object
   name = input("Enter your name:")
   password = input("Enter your password")
  
   # Initialize User object before date
   user = Article(name=name,
               uid=uid,
               password=password
               )
  
   # create user.dob, fail with today as dob
dob = input("Enter your date of birth 'YYYY-MM-DD'")
    try:
       article.dob = datetime.strptime(dob, '%Y-%m-%d').date()
    except ValueError:
       article.dob = datetime.today()
       print(f"Invalid date {dob} require YYYY-mm-dd, date defaulted to {user.dob}")
         
   # write object to database
   with app.app_context():
       try:
           object = user.create()
           print("Created\n", object.read())
       except:  # error raised if object not created
           print("Unknown error uid {uid}")
      
create()


# SQLAlchemy extracts all users from database, turns each user into JSON
def read():
   with app.app_context():
       table = User.query.all()
   json_ready = [user.read() for user in table] # "List Comprehensions", for each user add user.read() to list
   return json_ready


read()
