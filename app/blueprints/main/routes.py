from flask import render_template
from . import main as main_bp

@main_bp.route('/', methods=['Get'])
def index():
    return render_template('index.html.j2')
