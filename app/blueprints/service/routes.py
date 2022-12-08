from flask import  render_template, request, redirect, url_for, flash
from app.forms import ServiceForm
from flask_login import login_required,current_user
from .models import Service,Additional
from . import service_bp

@service_bp.route('/services', methods=['GET','POST'])
def services():
    form = ServiceForm()
    if request.method == 'POST' and form.validate_on_submit():
        sFoot=form.square_foot.data
        frequency=form.requested_service.data.lower()
        extras = form.extras.data
        print(sFoot,frequency,extras,type(sFoot))
        newService = Service(sFoot,frequency,user_id=current_user.id)
        newService.commit()
        serviceQuote,extrasQuote, = Service.costs[sFoot][frequency], sum( [int(extra.split('$')[-1]) for extra in extras] if extras else (0,0) ) 
        return render_template('services.html.j2',form = form, serviceQuote=serviceQuote, extrasQuote=extrasQuote)

    return render_template('services.html.j2',form = form)