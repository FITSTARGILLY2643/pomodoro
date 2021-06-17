from flask import render_template
from . import main
from ..models import User
from .. import db
from flask_login import login_required,current_user
# import datetime

@main.route('/')
def index():

    title = 'Home - Welcome to IbraFits Timer'
  
    return render_template('index.html',title = title,current_user=current_user)

@main.route('/timer')
def timer():

    title = 'Manage your time'
  
    return render_template('timer.html',title = title)
