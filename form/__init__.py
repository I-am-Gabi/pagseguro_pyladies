from flask import Flask
app = Flask(__name__)

import form.views

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/requests'
app.config['SECRET_KEY'] = 'hard to guess string' 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True