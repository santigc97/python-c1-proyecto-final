from flask import Blueprint, request, jsonify, current_app
from functools import wraps
from werkzeug.security import generate_password_hash
import jwt
from models import db, Usuario, Paciente, Doctor, Centro

admin_bp = Blueprint('admin_bp', __name__)


# comprueba que el token sea valido antes de entrar a la ruta
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


# ---- USUARIOS ----

@admin_bp.route('/admin/usuario', methods=['POST'])
@token_requerido
def crear_usuario(payload):
    if payload['rol'] != 'admin':
        return jsonify({'mensaje': 'Acceso denegado'}), 403

    datos = request.get_json()
    if not datos or 'username' not in datos or 'password' not in datos or 'rol' not in datos:
        return jsonify({'error': 'Faltan campos: username, password, rol'}), 400

    if Usuario.query.filter_by(username=datos['username']).first():
        return jsonify({'error': 'El usuario ya existe'}), 400

    nuevo = Usuario(username=datos['username'], password=generate_password_hash(datos['password']), rol=datos['rol'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado', 'id': nuevo.id}), 201


# ---- DOCTORES ----

@admin_bp.route('/admin/doctores', methods=['POST'])
@token_requerido
def crear_doctor(payload):
    if payload['rol'] != 'admin':
        return jsonify({'mensaje': 'Acceso denegado'}), 403

    datos = request.get_json()
    if not datos or 'nombre' not in datos:
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    nuevo = Doctor(nombre=datos['nombre'], especialidad=datos.get('especialidad', ''))
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Doctor creado', 'id': nuevo.id}), 201


@admin_bp.route('/admin/doctores', methods=['GET'])
@token_requerido
def obtener_doctores(payload):
    doctores = Doctor.query.all()
    return jsonify([{'id': d.id, 'nombre': d.nombre, 'especialidad': d.especialidad} for d in doctores])


@admin_bp.route('/admin/doctores/<int:id>', methods=['GET'])
@token_requerido
def obtener_doctor(payload, id):
    d = Doctor.query.get_or_404(id)
    return jsonify({'id': d.id, 'nombre': d.nombre, 'especialidad': d.especialidad})


# ---- PACIENTES ----

@admin_bp.route('/admin/pacientes', methods=['POST'])
@token_requerido
def crear_paciente(payload):
    if payload['rol'] != 'admin':
        return jsonify({'mensaje': 'Acceso denegado'}), 403

    datos = request.get_json()
    if not datos or 'nombre' not in datos:
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    nuevo = Paciente(nombre=datos['nombre'], telefono=datos.get('telefono', ''), estado='ACTIVO')
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Paciente creado', 'id': nuevo.id}), 201


@admin_bp.route('/admin/pacientes', methods=['GET'])
@token_requerido
def obtener_pacientes(payload):
    pacientes = Paciente.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'telefono': p.telefono, 'estado': p.estado} for p in pacientes])


@admin_bp.route('/admin/pacientes/<int:id>', methods=['GET'])
@token_requerido
def obtener_paciente(payload, id):
    p = Paciente.query.get_or_404(id)
    return jsonify({'id': p.id, 'nombre': p.nombre, 'telefono': p.telefono, 'estado': p.estado})


# ---- CENTROS ----

@admin_bp.route('/admin/centros', methods=['POST'])
@token_requerido
def crear_centro(payload):
    if payload['rol'] != 'admin':
        return jsonify({'mensaje': 'Acceso denegado'}), 403

    datos = request.get_json()
    if not datos or 'nombre' not in datos:
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    nuevo = Centro(nombre=datos['nombre'], direccion=datos.get('direccion', ''))
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Centro creado', 'id': nuevo.id}), 201


@admin_bp.route('/admin/centros', methods=['GET'])
@token_requerido
def obtener_centros(payload):
    centros = Centro.query.all()
    return jsonify([{'id': c.id, 'nombre': c.nombre, 'direccion': c.direccion} for c in centros])


@admin_bp.route('/admin/centros/<int:id>', methods=['GET'])
@token_requerido
def obtener_centro(payload, id):
    c = Centro.query.get_or_404(id)
    return jsonify({'id': c.id, 'nombre': c.nombre, 'direccion': c.direccion})
