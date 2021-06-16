from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
from flask_uploads import UploadSet,IMAGES,configure_uploads
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
# loginManager= LoginManager()
# loginManager.session_protection='strong'
# loginManager.login_view('auth.login')
photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    # loginManager.init_app(app)

    configure_uploads(app,photos)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app







