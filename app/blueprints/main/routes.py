from flask import render_template
from flask_login import login_required
from . import main as main_bp

@main_bp.route('/', methods=['Get'])
def index():
    return render_template('index.html.j2')

@main_bp.route('/', methods=['GET','POST'])
@login_required
def reviews():
    render_template('reviews.html.j2')
