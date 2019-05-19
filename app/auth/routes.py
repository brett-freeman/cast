from flask import render_template, redirect, url_for, flash, g, request
from flask_login import login_required, current_user
from .forms import LoginForm, SignupForm
from . import auth

@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user')
        return redirect('/')
    return render_template('auth/login.html', title='Sign In', form=form)

@auth.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for user')
        return redirect('/')
    return render_template('auth/signup.html', title='Sign Up', form=form)
