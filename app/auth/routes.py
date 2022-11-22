from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from app.forms import LoginForm
from app.models import User,db 
from flask_login import login_required,login_user

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup',methods = ['GET','POST'])
def login():
    form= LoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data.lower()
            password = form.password.data
            print(email,password)

            logged_user = User.query.filter(User.email== email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash(f'{logged_user.username}You were successfully logged in', 'auth-success')
                return redirect(url_for('site.profile'))

            else:
                flash('Your Email/Password is incorrect', 'auth-failed')
                return render_template('signin.html',loginerror='Your Email/Password is incorrect', form=form)
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')
    
    return render_template('signin.html', form = form)
   