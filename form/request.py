#!/usr/bin/env python
# encoding: utf-8
""" 
"""
 
# Forms WTF
from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, StringField, SubmitField
from wtforms import validators
from wtforms.validators import Required

class formRequest(Form):
  name = StringField('Nome', [validators.Required()]) 
  email = StringField('Email', [validators.Required()])  
  phone = StringField('Telefone', [validators.Required()]) 
  cpf = StringField('CPF', [validators.Required()]) 
  street = StringField('Rua', [validators.Required()])  
  number = StringField('Número', [validators.Required()]) 
  complement = StringField('Complemento', [validators.Required()])  
  district = StringField('Bairro', [validators.Required()]) 
  postal_code = StringField('CEP', [validators.Required()]) 
  city = StringField('Cidade', [validators.Required()])   	
  state = StringField('Estado', [validators.Required()])   
  submit = SubmitField('Comprar!', [validators.Required()])