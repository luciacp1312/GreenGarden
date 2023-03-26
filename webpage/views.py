from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .database import Volunteer, User
#from .database import classIWantToImport
from . import db
import re

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required # we need to be logged to access this page
def home():

    return render_template("home.html", user=current_user)

@views.route('/frequent_questions', methods=['GET', 'POST'])
@login_required
def freq_quest():

    return render_template("freqQuest.html", user=current_user)

@views.route('/vegetables_info', methods=['GET', 'POST'])
@login_required
def veg_info():

    return render_template("vegInfo.html", user=current_user)

@views.route('/volunteers', methods=['GET', 'POST'])
@login_required
def volunteers():
    if request.method == 'POST':
        phone = request.form.get('phone')
        postalCode = request.form.get('postalCode')
        #email = request.form.get('email')
        startDate = request.form.get('startDate') # poner que tiene que ser antes que el endDate
        endDate = request.form.get('endDate')
        
        if not phone.isdigit():
            flash('Phone number must be an integer', category='error')
        elif not postalCode.isdigit():
            flash('Postal code must be an integer', category='error')
        elif startDate=='':
            flash('Start Date hasn\'t been selected', category='error') # startDate tiene que ser antes de endDate, y tiene que ser a partir del día actual
        elif endDate=='':
            flash('End Date hasn\'t been selected', category='error') # endDate tiene que ser después de startDate, y podemos indicar que sea hasta un máximo de 1 año
        else:
            flash('Your form has been successfully created. An email/phone message will be sent to you as soon as possible with possible dates', category='success')
            
    return render_template("volunteers.html", user=current_user)

@views.route('/partnerships', methods=['GET', 'POST'])
@login_required
def partnerships():

    return render_template("partnerships.html", user=current_user)

@views.route('/terms', methods=['GET', 'POST'])
@login_required
def terms():

    return render_template("terms.html", user=current_user)