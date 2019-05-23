from functools import wraps
from flask import Blueprint, redirect, flash, url_for
from flask_login import current_user

admin = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('That required admin.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

from . import routes
