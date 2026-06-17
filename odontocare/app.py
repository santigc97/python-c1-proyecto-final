from flask import Flask
from models import db
from auth_routes import auth_bp
from admin_routes import admin_bp
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta_odontocare'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///odontocare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # creo el admin por defecto si no existe
        from models import Usuario
        if not Usuario.query.filter_by(username='admin').first():
            admin = Usuario(
                username='admin',
                password=generate_password_hash('admin123'),
                rol='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print('Usuario admin creado: admin / admin123')

    app.run(debug=True, host='0.0.0.0', port=5000)
