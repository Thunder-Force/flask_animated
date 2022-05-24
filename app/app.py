
import bcrypt

import config
import os
#import psycopg2

from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
#from numpy import NaN, int64
#from model import user_ip_loc, json_encoder

# INIT APP
#===============================================================
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='template')
app.secret_key = config.S_KEY
root_path = os.getcwd()
#conn = psycopg2.connect(host=config.HOST, database=config.DB, user=config.USER, password=config.PW)


#=====================================================================================================
# ROUTES
#=====================================================================================================


# [ROOT]: PRE-AUTH
#=============================================================== 
def user_authentication(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return function(*args, **kwargs)
    return decorated_function



# [ROOT]: INDEX-TEST
#===============================================================
@app.route('/')
def index1():
    return render_template('index.html')

# [ROOT]: INDEX
#===============================================================
@app.route('/a')
def index():
    if 'email' in session:
        return redirect(url_for('Dashboard'))
    else:    
        return redirect(url_for('login'))


# [ROOT]: ERROR 404
#===============================================================
@app.errorhandler(404)
def not_found(e):
  return render_template('module/error_404.html'), 404


# [ACCOUNT]: LOGIN
#===============================================================
@app.route('/account/login/', methods=['GET', 'POST'])
def login():
    return render_template('account/login.html', company = config.COMPANY_NAME)


# [ACCOUNT]: LOGOUT
#===============================================================
@app.route('/account/logout/')
def logout():
   session.clear()
   return redirect(url_for('login'))


# [ACCOUNT]: RECOVERY
#===============================================================
@app.route('/account/recover/')
def recover():
   return render_template('account/recover.html', company = config.COMPANY_NAME)


# [ACCOUNT]: REGISTER
#===============================================================
@app.route('/account/register/', methods=['GET', 'POST'])
def register():
    return render_template('account/register.html', company = config.COMPANY_NAME)


# [DASHBOARD]
#===============================================================
@app.route('/dashboard/')
@user_authentication
def dashboard():
    return render_template('dashboard.html')




# [USER]: HELP
#===============================================================
@app.route('/user/help/')
def help():
    return render_template('user/help.html')


# [USER]: PROFILE
#===============================================================
@app.route('/user/profile/')
@user_authentication
def user_profile():
    return render_template('user/profile.html')



# [USER]: PRIVACY
#===============================================================
@app.route('/user/privacy/')
def user_privacy():
    return render_template('user/privacy.html')


# [USER]: SETTINGS
#===============================================================
@app.route('/user/settings/')
@user_authentication
def user_settings():
    return render_template('user/settings.html')


# [USER]: SUPPORT
#===============================================================
@app.route('/user/support/')
def user_support():
    return render_template('user/support.html')

# [USER]: TERMS
#===============================================================
@app.route('/user/terms/')
def user_terms():
    return render_template('user/terms.html')



#=====================================================================================================
# MAIN
#=====================================================================================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))