from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    motivo = db.Column(db.String(200))
    estado = db.Column(db.String(20), default='PROGRAMADA')
    id_paciente = db.Column(db.Integer, nullable=False)
    id_doctor = db.Column(db.Integer, nullable=False)
    id_centro = db.Column(db.Integer, nullable=False)
    id_usuario_registra = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cita {self.id} - {self.fecha}>'
