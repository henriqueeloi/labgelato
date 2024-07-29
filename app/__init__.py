from flask import Flask

from config import Config
from app.extensions import db
from app.main import bp as main_bp
from app.ingredients import bp as ingredients_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    app.secret_key = '\xd9\xad\xbb\xd7\xf3z\x87\x1a,\xadh\xb3\xbf/\x97\x8b?\xc3P^\x0e?\xb2V'

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(main_bp)

    app.register_blueprint(ingredients_bp, url_prefix='/ingredients')
    return app
