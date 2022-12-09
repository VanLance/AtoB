from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm
from .models import User
from flask_login import login_required, login_user, current_user, logout_user
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            logged_user = User.query.filter(User.email == form.email.data.lower()).first()
            if logged_user and logged_user.check_password(form.password.data):
                login_user(logged_user)
                flash(f'{logged_user.first_name}You were successfully logged in', 'success')
                return redirect(url_for('main.index'))
            else:
                flash('Your Email/Password is incorrect', 'failed')
                return render_template('login.html.j2', loginerror='Your Email/Password is incorrect', form=form)
          
    except:
        flash('Your Email/Password is incorrect', 'failed')
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('login.html.j2', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        check_user = User.query.filter(User.email == form.email.data.lower()).first()
        if not check_user:
            new_user = User(first_name=form.first_name.data.lower(),last_name=form.last_name.data.lower(), email=form.email.data.lower())
            new_user.hash_password(form.password.data)
            new_user.commit()
            return redirect(url_for('auth.login'))
        flash('Email already in use', 'warning')
        return render_template('register.html.j2', registererror='Email already in use', form=form)
    return render_template('register.html.j2', form=form)


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have successfully logged yourself out.','success')
    return redirect(url_for('main.index'))
