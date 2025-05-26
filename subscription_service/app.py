from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

# Import routes to register blueprints
from routes.auth import auth_bp
from routes.plans import plans_bp
from routes.subscriptions import subs_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(plans_bp, url_prefix='/plans')
app.register_blueprint(subs_bp, url_prefix='/subscriptions')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # create tables on first run
    app.run(debug=True)
