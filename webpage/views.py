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