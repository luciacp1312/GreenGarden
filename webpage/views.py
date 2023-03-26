from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .database import Volunteer
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
        phone = request.form.get('phoneContact')
        postalCode = request.form.get('postalCode')
        #startDate = request.form.get('startDate') # poner que tiene que ser antes que el endDate
        #endDate = request.form.get('endDate')
        
        if phone is None:
            flash('Phone is None', category='error')
        elif not phone.isdigit():
            flash('Phone number must be an integer', category='error')
        else:
            flash('Phone is correct', category='success')
            
        if postalCode is None:
            flash('postalCode is None', category='error')
        elif not postalCode.isdigit():
            flash('postalCode must be an integer', category='error')
        else:
            flash('postalCode is correct', category='success')
            
    return render_template("volunteers.html", user=current_user)

@views.route('/partnerships', methods=['GET', 'POST'])
@login_required
def partnerships():

    return render_template("partnerships.html", user=current_user)

@views.route('/terms', methods=['GET', 'POST'])
@login_required
def terms():

    return render_template("terms.html", user=current_user)