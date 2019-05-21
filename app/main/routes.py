from flask import render_template
from flask_login import login_required
from app import db

from . import main

@main.route('/')
#@login_required
def index():
    return render_template('main/index.html', title='Index')
