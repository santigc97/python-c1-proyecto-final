from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # admin, medico, secretaria, paciente

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    estado = db.Column(db.String(10), default='ACTIVO')

    def __repr__(self):
        return f'<Paciente {self.nombre}>'


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100))

    def __repr__(self):
        return f'<Doctor {self.nombre}>'


class Centro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))

    def __repr__(self):
        return f'<Centro {self.nombre}>'
