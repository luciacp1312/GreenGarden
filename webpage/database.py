from . import db
from flask_login import UserMixin # This will give the users some things specific for flask login
import uuid

# In this class we create our database, that will later be loaded in the instance folder as database.db

class User(db.Model, UserMixin): # UserMixin is needed to access all the information about the User in other files
    id = db.Column(db.Integer, primary_key=True) # Type, PK
    email = db.Column(db.String(150), unique=True) # Type, Uniqueness
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    requests = db.relationship('Request') 
    

    
class Request(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    postalCode = db.Column(db.String(10), nullable=False)
    startDate = db.Column(db.Date, nullable=True)
    endDate = db.Column(db.Date, nullable=True)
    consider = db.Column(db.String(250), nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

def __init__(self, name, email, phone, city, country, postalCode, startDate=None, endDate=None, consider=None, userId=None):
    self.name = name
    self.email = email
    self.phone = phone
    self.city = city
    self.country = country
    self.postalCode = postalCode
    self.startDate = startDate
    self.endDate = endDate
    self.consider = consider
    self.userId = userId
    if id is None:
        self.id = str(uuid.uuid4()) # To create a random ID number for the request
    else:
        self.id = id
    
    # 1 user can have 0 or more requests: 1-M relationship

# TO CREATE 1-M RELATIONSHIP:
# In the MANY part we put:
# paramName = db.Column(db.TypeOfId, db.ForeignKey('NameOfTheOtherClass.idName'))
# e.g:  userId = db.Column(db.Integer, db.ForeignKey('user.id'))    #This would be in Company
    
#In the ONE part we put:
# paramName = db.relationship('NameOfTheOtherClass')
# e.g:  company = db.relationship('Company')                        #This would be in User
# a function that gets the current date and time:
# date = db.Column(db.DateTime(timezone=True), default=func.now())