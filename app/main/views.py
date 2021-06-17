from flask import render_template,redirect,url_for,abort,request
from . import forms
from . import main



@main.route('/')
def index():

    title = 'Home - Welcome to IbraFits Timer'

    return render_template('index.html',title = title)
