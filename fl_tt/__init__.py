from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from fl_tt.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# Where the login route is located. Function name of our route: 'login'
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from fl_tt.users.routes import users
    from fl_tt.posts.routes import posts
    from fl_tt.main.routes import main
    from fl_tt.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app