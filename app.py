from flask import Flask
from flask_login import LoginManager
from models.model import db, User
from datetime import timedelta
from flask_session import Session

app = None
login_manager = LoginManager()

def create_app():
  app = Flask(__name__, template_folder="templates")
  

  app.config['SECRET_KEY'] = 'jkn8u9enfviuewhhnv8472489bfe49yh43JGe9j93GJR'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SRMGrade.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Server-side session management
  app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions on the server
  app.config['SESSION_PERMANENT'] = False  # Session won't expire automatically unless configured
  app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

  login_manager.init_app(app)
  db.init_app(app)
  Session(app)

  app.app_context().push()

  return app



app = create_app()

# tocreate the table
# with app.app_context():  
#   db.drop_all()
#   db.create_all()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


from controllers.user_controller import *
from controllers.admin_controller import *
from controllers.login_signup import *
from controllers.error_handler import *

if __name__ == '__main__':
  app.run()
