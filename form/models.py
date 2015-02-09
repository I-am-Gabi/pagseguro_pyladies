#!/usr/bin/env python
# encoding: utf-8 

# SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy 
from form import app

db = SQLAlchemy(app)

class Requests(db.Model):
	__tablename__ = 'requests'

  	id = db.Column(db.Integer, primary_key = True)
  	name = db.Column(db.String(80)) 
  	email = db.Column(db.String(50)) 
  	phone = db.Column(db.String(15)) 
  	cpf = db.Column(db.String(20)) 
  	street = db.Column(db.String(150)) 
  	number = db.Column(db.String(10)) 
  	complement = db.Column(db.String(150)) 
  	district = db.Column(db.String(20)) 
  	postal_code = db.Column(db.String(20)) 
  	city = db.Column(db.String(20))
  	state = db.Column(db.String(20))   

        def __init__(self, name, email, phone, cpf, street, number, complement, district, postal_code, city, state):
            self.name = name
            self.email = email
            self.phone = phone
            self.cpf = cpf
            self.street = street
            self.number = number
            self.complement = complement
            self.district = district
            self.postal_code = postal_code
            self.city = city
            self.state = state 
 