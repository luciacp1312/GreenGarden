from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .database import Request
import uuid
#from .database import classIWantToImport
from . import db
from datetime import datetime

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
        name = request.form.get('companyName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        country = request.form.get('country')
        postalCode = request.form.get('postalCode')
        startDate_str = request.form.get('startDate') # poner que tiene que ser antes que el endDate
        endDate_str = request.form.get('endDate')
        consider = request.form.get('consider')
           
        startDate = ''
        endDate = ''
        if not phone.isdigit():
            flash('Phone number must be an integer', category='error')
        elif not postalCode.isdigit():
            flash('Postal code must be an integer', category='error')
        elif not startDate_str=='' and not endDate_str=='':
            startDate = datetime.strptime(startDate_str, '%Y-%m-%d').date()
            endDate = datetime.strptime(endDate_str, '%Y-%m-%d').date()
            if startDate < datetime.now().date() or endDate < datetime.now().date():
                flash('The dates have to be set after the current date', category='error')
            elif startDate > endDate:
                flash('The start date must be the same or before the end date', category='error')
        else:
            id_number = uuid.uuid4() # To create a random ID number for the request
            
            # POR ALGÚN MOTIVO, NO ME ESTÁ GUARDANDO EL NAME (SALE COMO NONE)
            if startDate=='' and endDate=='':
                new_petition = Request(id=str(id_number), name=name, email=email, phone=phone, city=city, country=country, postalCode=postalCode, consider=consider, userId=current_user.id)
            elif startDate=='':
                new_petition = Request(id=str(id_number), name=name, email=email, phone=phone, city=city, country=country, postalCode=postalCode, endDate=endDate, consider=consider, userId=current_user.id)
            elif endDate=='':
                new_petition = Request(id=str(id_number), name=name, email=email, phone=phone, city=city, country=country, postalCode=postalCode, startDate=startDate, consider=consider, userId=current_user.id)
            else:
                new_petition = Request(id=str(id_number), name=name, email=email, phone=phone, city=city, country=country, postalCode=postalCode, startDate=startDate, endDate=endDate, consider=consider, userId=current_user.id)
            db.session.add(new_petition)
            db.session.commit()
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