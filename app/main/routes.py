from flask import render_template
from app import db

from . import main

@main.route('/')
def index():
    return render_template('main/index.html', title='Index')
