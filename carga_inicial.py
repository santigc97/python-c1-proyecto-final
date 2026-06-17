import csv
import json
import requests

API_URL = 'http://localhost:5000'
CITAS_URL = 'http://localhost:5001'


def login():
    respuesta = requests.post(f'{API_URL}/auth/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    datos = respuesta.json()
    if 'token' not in datos:
        print('Error al hacer login:', datos)
        return None
    print('Login exitoso')
    return datos['token']


def cargar_datos(token):
    cabeceras = {'Authorization': f'Bearer {token}'}
    id_doctor = None
    id_paciente = None
    id_centro = None

    with open('datos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            tipo = fila['tipo']

            if tipo == 'doctor':
                respuesta = requests.post(
                    f'{API_URL}/admin/doctores',
                    json={'nombre': fila['nombre'], 'especialidad': fila['campo1']},
                    headers=cabeceras
                )
                resultado = respuesta.json()
                print(f'Doctor creado: {resultado}')
                if id_doctor is None:
                    id_doctor = resultado.get('id')

            elif tipo == 'paciente':
                respuesta = requests.post(
                    f'{API_URL}/admin/pacientes',
                    json={'nombre': fila['nombre'], 'telefono': fila['campo2']},
                    headers=cabeceras
                )
                resultado = respuesta.json()
                print(f'Paciente creado: {resultado}')
                if id_paciente is None:
                    id_paciente = resultado.get('id')

            elif tipo == 'centro':
                respuesta = requests.post(
                    f'{API_URL}/admin/centros',
                    json={'nombre': fila['nombre'], 'direccion': fila['campo1']},
                    headers=cabeceras
                )
                resultado = respuesta.json()
                print(f'Centro creado: {resultado}')
                if id_centro is None:
                    id_centro = resultado.get('id')

    return id_doctor, id_paciente, id_centro


def crear_cita(token, id_doctor, id_paciente, id_centro):
    cabeceras = {'Authorization': f'Bearer {token}'}
    respuesta = requests.post(
        f'{CITAS_URL}/citas',
        json={
            'fecha': '2025-09-01 10:00',
            'motivo': 'Revision general',
            'id_paciente': id_paciente,
            'id_doctor': id_doctor,
            'id_centro': id_centro
        },
        headers=cabeceras
    )
    return respuesta.json()


token = login()

if token:
    id_doctor, id_paciente, id_centro = cargar_datos(token)

    print('\nCreando cita de prueba...')
    cita = crear_cita(token, id_doctor, id_paciente, id_centro)

    print('\nCita creada:')
    print(json.dumps(cita, indent=2, ensure_ascii=False))
