from flask import render_template, redirect, url_for, flash, g, request
from flask_login import login_required, current_user, login_user, logout_user

from . import auth
from .forms import LoginForm, RegisterForm

from app import db
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
        next_page = request.args.get('next')

        # Redirect the user where they came from 
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@auth.route('/register', methods=('GET', 'POST'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks, you are now registered!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
