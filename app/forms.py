from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email=StringField('Email Address', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must Match")])
    submit = SubmitField('Register')

class ServiceForm(FlaskForm):
    requested_service =  SelectField("Requested Service", choices=['Weekly', 'Biweekly', 'Deep Clean'],validators=[DataRequired()])
    square_foot =  SelectField("Square Foot", choices=['600','1000','1200','1500','1800','2000','2500','3000','4000','5000','6000'], validators=[DataRequired()])
    extras =  SelectMultipleField("Extras", choices=['Polishing: $25','Cabinets: $20','Base Boards: $25','Refridgerator: $15','Windows: $4','Skylights: $8','Shampoo Carpets: $40'], coerce=str, option_widget=None)
    submit = SubmitField('Submit Service')

