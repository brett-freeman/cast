from . import admin
from flask_login import login_required

@admin.route('/admin')
@login_required
def admin():
    return 'Hey this is some admin shit yo'
