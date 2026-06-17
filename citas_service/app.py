from flask import Flask
from models import db
from citas_routes import citas_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta_odontocare'  # tiene que ser igual que en odontocare
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(citas_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=5001)
