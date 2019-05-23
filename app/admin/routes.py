from . import admin, admin_required
from flask_login import login_required

@admin.route('/admin')
@login_required
@admin_required
def admin():
    return 'Hey this is some admin shit yo'
