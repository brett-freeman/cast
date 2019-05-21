from flask import render_template, redirect, url_for, flash, g, request
from flask_login import login_required, current_user, login_user
from .forms import LoginForm, SignupForm
from . import auth
from app.models import User

@auth.route('/login', methods=('GET', 'POST'))
def login():
    # Redirect user to index if they are already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # Return to login if username is not found or password is wrong
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return(redirect(url_for('main.index')))
    return render_template('auth/login.html', title='Sign In', form=form)

@auth.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for user')
        return redirect('/')
    return render_template('auth/signup.html', title='Sign Up', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
