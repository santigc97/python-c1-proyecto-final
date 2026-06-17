from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
import jwt
import datetime
from models import Usuario

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    datos = request.get_json()

    if not datos or 'username' not in datos or 'password' not in datos:
        return jsonify({'error': 'Usuario y contraseña son obligatorios'}), 400

    usuario = Usuario.query.filter_by(username=datos['username']).first()

    if not usuario or not check_password_hash(usuario.password, datos['password']):
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

    # genero el token con 2 horas de duracion
    payload = {
        'sub': usuario.username,
        'rol': usuario.rol,
        'id': usuario.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token, 'rol': usuario.rol})
