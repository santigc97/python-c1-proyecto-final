from flask import Blueprint, request, jsonify, current_app
from functools import wraps
import jwt
from models import db, Cita

citas_bp = Blueprint('citas_bp', __name__)


def token_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401

        token = auth_header.split(" ")[1]  # quito el "Bearer"

        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(payload, *args, **kwargs)
    return wrapper


@citas_bp.route('/citas', methods=['POST'])
@token_requerido
def crear_cita(payload):
    datos = request.get_json()

    if not datos or 'fecha' not in datos or 'id_paciente' not in datos or 'id_doctor' not in datos or 'id_centro' not in datos:
        return jsonify({'error': 'Faltan campos: fecha, id_paciente, id_doctor, id_centro'}), 400

    # compruebo que el doctor no tenga ya una cita a esa hora
    cita_existente = Cita.query.filter_by(id_doctor=datos['id_doctor'], fecha=datos['fecha'], estado='PROGRAMADA').first()
    if cita_existente:
        return jsonify({'error': 'El doctor ya tiene una cita en esa fecha y hora'}), 400

    nueva_cita = Cita(
        fecha=datos['fecha'],
        motivo=datos.get('motivo', ''),
        estado='PROGRAMADA',
        id_paciente=datos['id_paciente'],
        id_doctor=datos['id_doctor'],
        id_centro=datos['id_centro'],
        id_usuario_registra=payload['id']
    )
    db.session.add(nueva_cita)
    db.session.commit()

    return jsonify({
        'mensaje': 'Cita creada con éxito',
        'cita': {
            'id': nueva_cita.id,
            'fecha': nueva_cita.fecha,
            'motivo': nueva_cita.motivo,
            'estado': nueva_cita.estado,
            'id_paciente': nueva_cita.id_paciente,
            'id_doctor': nueva_cita.id_doctor,
            'id_centro': nueva_cita.id_centro
        }
    }), 201


@citas_bp.route('/citas', methods=['GET'])
@token_requerido
def obtener_citas(payload):
    rol = payload['rol']

    # filtro segun el rol
    if rol in ['admin', 'secretaria']:
        citas = Cita.query.all()
    elif rol == 'medico':
        citas = Cita.query.filter_by(id_usuario_registra=payload['id']).all()
    else:
        citas = Cita.query.filter_by(id_paciente=payload['id']).all()

    return jsonify([{
        'id': c.id,
        'fecha': c.fecha,
        'motivo': c.motivo,
        'estado': c.estado,
        'id_paciente': c.id_paciente,
        'id_doctor': c.id_doctor,
        'id_centro': c.id_centro
    } for c in citas])


@citas_bp.route('/citas/<int:id>', methods=['PUT'])
@token_requerido
def cancelar_cita(payload, id):
    cita = Cita.query.get_or_404(id)

    if cita.estado == 'CANCELADA':
        return jsonify({'mensaje': 'La cita ya está cancelada'}), 400

    cita.estado = 'CANCELADA'
    db.session.commit()
    return jsonify({'mensaje': 'Cita cancelada', 'id': cita.id, 'estado': cita.estado})
