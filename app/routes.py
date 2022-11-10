from flask import render_template, request
import requests 
from .forms import LoginForm, RegisterForm
from app import app

@app.route('/', methods=['Get'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # LOGIN THE USER HERE
        email = form.email.data.lower()
        password = form.password.data

        if email in app.config.get('REGISTERED_USERS') and \
            password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            #Login Success!!!
            return f"Login Success Welcome { app.config.get('REGISTERED_USERS').get(email).get('name') }"
        error_string = "Incorrect Email/Password Combo"
        return render_template('login.html.j2', loginerror=error_string, form=form)
    return render_template('login.html.j2', form=form)

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        return "Welcome To our App... Thanks for registering"
    return render_template('register.html.j2', form=form)