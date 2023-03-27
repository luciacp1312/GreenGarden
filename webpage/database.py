from . import db
from flask_login import UserMixin # This will give the users some things specific for flask login
from sqlalchemy.sql import func

# In this class we create our database, that will later be loaded in the instance folder as database.db

class User(db.Model, UserMixin): # UserMixin is needed to access all the information about the User in other files
    id = db.Column(db.Integer, primary_key=True) # Type, PK
    email = db.Column(db.String(150), unique=True) # Type, Uniqueness
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    requests = db.relationship('Request') 
    
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    postalCode = db.Column(db.String(10), nullable=False)
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    consider = db.Column(db.String(250))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    
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