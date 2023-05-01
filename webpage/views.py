from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .database import Request
import uuid
#from .database import classIWantToImport
from . import db
from datetime import datetime, time

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


def validate_date_string(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format', category='error')
        return None
    return date

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
        startDate_str = request.form.get('startDate')
        endDate_str = request.form.get('endDate')
        consider = request.form.get('consider')
        send = False
        afterToday = True
           
        startDate = None
        endDate = None
        
        try:
            phone_int = int(phone)
            postalCode_int = int(postalCode)
        except ValueError:
            send = False
            flash('Phone number and postal code must be integers', category='error')
        else:
            if startDate_str:
                try:
                    startDate = datetime.strptime(startDate_str, '%Y-%m-%d')
                except ValueError:
                    flash('Invalid start date format', category='error')
                    send = False
                else:
                    today = datetime.now().date()
                    if startDate.date() < today:
                        send = False
                        afterToday = False
                        flash('Start date must be after today', category='error')
                    else:
                        send = True
                        startDate = datetime.combine(startDate.date(), time.min) # convert to datetime.datetime object
            else:
                send = True
                startDate = datetime.now()

            if endDate_str:
                try:
                    endDate = datetime.strptime(endDate_str, '%Y-%m-%d')
                except ValueError:
                    send = False
                    flash('Invalid end date format', category='error')
                else:
                    if endDate.date() < startDate.date():
                        send = False
                        flash('End date must be after start date', category='error')
                    else:
                        send = True
            else:
                send = True
                endDate = startDate
            
        if not afterToday:
            send = False 
            
        if send:
            new_petition = Request(id=str(uuid.uuid4()), name=name, email=email, phone=phone, city=city, country=country, postalCode=postalCode, startDate=startDate, endDate=endDate, consider=consider, userId=current_user.id)
            db.session.add(new_petition)
            db.session.commit()
            flash('Your form has been successfully created. An email/phone message will be sent to you as soon as possible with possible dates', category='success')
        else:
            flash('There has been a problem with the form', category='error')
    return render_template("volunteers.html", user=current_user)

@views.route('/partnerships', methods=['GET', 'POST'])
@login_required
def partnerships():

    return render_template("partnerships.html", user=current_user)

@views.route('/terms', methods=['GET', 'POST'])
@login_required
def terms():

    return render_template("terms.html", user=current_user)