# -*- coding: utf-8 -*-
from form import app 
from form.models import Requests, db
from request import formRequest
from flask import session
from flask import jsonify
from flask import request
from flask import redirect
from flask import render_template
from pagseguro import PagSeguro

@app.route('/', methods=['GET', 'POST'])
def index():  
	formulario = formRequest()
	if request.method == 'POST' and formulario.name.data!='':
		# add no banco de dados
		name = formulario.name.data
		email = formulario.email.data
		phone = formulario.phone.data
		cpf = formulario.cpf.data
		street = formulario.street.data
		number = formulario.number.data
		complement = formulario.complement.data
		district = formulario.district.data
		postal_code = formulario.postal_code.data 
		city = formulario.city.data	
		state = formulario.state.data
		newRequest = Requests(name, email, phone, cpf, street, number, complement, district, postal_code, city, state)  
		db.session.add(newRequest)
		db.session.commit()   
 		# fazer compra
		sender = {
        	"name": name,
        	"email": email,
        	"phone": phone 
        }
		shipping = {
		    "street": street,
		    "number": number,
		    "complement": complement,
		    "district": district,
		    "postal_code": postal_code,
		    "city": city,
		    "state": state,
		    "country": 'BRA'
		}
		pg = checkout_pg(sender, shipping, newRequest)
		response = pg.checkout()
		print 'responde url %s' % response.payment_url
		return redirect(response.payment_url) 
	return render_template('index.jinja2', form=formulario)

def checkout_pg(sender, shipping, request):
    pg = PagSeguro(email=app.config['EMAIL'], token=app.config['TOKEN'])
    pg.sender = sender
    shipping['type'] = pg.SEDEX
    pg.shipping = shipping
    pg.extra_amount = "%.2f" % float(app.config['EXTRA_AMOUNT'])
    pg.redirect_url = app.config['REDIRECT_URL']
    pg.notification_url = app.config['NOTIFICATION_URL']
    pg.add_item(id=request.id, description="Tshirt", amount=30.00, quantity=1, weight=0)
    print 'ok'
    return pg


@app.route('/confirmacao')
def confirmacao(): 
	return render_template('fim.jinja2')

@app.route('/notification')
def notification_view(request):
    notification_code = request.POST['notificationCode']
    pg = PagSeguro(email=app.config['EMAIL'], token=app.config['TOKEN'])
    pg.check_notification(notification_code)
    # use the return of the function above to update the order