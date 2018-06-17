# __init__.py


# IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vagrant:123456789@localhost/catalog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''
# import a blueprint that we will create
from project.user.views import owners_blueprint

# register our blueprints with the application
app.register_blueprint(user_blueprint, url_prefix='/user')
'''
@app.route('/')
def root():
    return "HELLO BLUEPRINTS!"