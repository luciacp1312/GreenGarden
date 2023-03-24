from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
#from .database import classIWantToImport
from . import db
import json

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

    return render_template("volunteers.html", user=current_user)

@views.route('/partnerships', methods=['GET', 'POST'])
@login_required
def partnerships():

    return render_template("partnerships.html", user=current_user)