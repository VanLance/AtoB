from flask import  render_template, request, redirect, url_for, flash
from app.forms import ServiceForm
from flask_login import login_required,current_user
from .models import Service,Additional
from . import service_bp

@service_bp.route('/services', methods=['GET','POST'])
@login_required
def services():
    form = ServiceForm()
    if request.method == 'POST' and form.validate_on_submit():
        sFoot=form.square_foot.data
        frequency=form.requested_service.data.lower()
        extras = form.extras.data
        print(sFoot,frequency,extras,type(sFoot))
        newService = Service(sFoot,frequency,user_id=current_user.id)
        newService.commit()
        print(extras)
        additionals = Additional()
        additionals.my_init([extra.split()[0].lower() for extra in extras])
        additionals.owner = current_user.id
        extrasQuote = sum([int(extra.split('$')[-1]) for extra in extras] if extras else (0,0) ) 
        additionals.quote =extrasQuote
        additionals.commit()
        
        flash(f'Your quote for service is: {newService.quote}', "success")
        flash(f'Additonal services: {extrasQuote}', "success")
    return render_template('services.html.j2',form = form)