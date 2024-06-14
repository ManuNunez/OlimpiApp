from functools import wraps
from flask import redirect, url_for, session, flash

def login_required(f):
    @wraps(f):
    def decorator(*args, **kwargs):
        if'user_id' not in session:
            flash("Necesitas iniciar sesion", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorator