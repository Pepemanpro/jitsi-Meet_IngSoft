from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template
from CrudBD_Usuarios import buscar_usuarios
from CrudBD_Usuarios import leer_usuarios, crear_usuario
from CrudBD_Videoconferencias import crear_videoconferencia, eliminar_videoconferencia,actualizar_videoconferencia
from CrudBD_Participantes import agregar_participante,eliminar_meet
from CrudBD_Participantes import obtener_participantes,eliminar_participante


app = Flask(__name__)

# Base de datos de usuarios (simulada)
CORS(app, resources={r"/": {"origins": ""}})
@app.route('/')
def root():
    return '<h1>Hello World</h1>'

# Ruta para el login (GET)
@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    #data = request.json
    #email = data.get('email')
    #password = data.get('password')
    usuario = buscar_usuarios(email)
    print(email)
    print(password)
    print(usuario)
    if(usuario[3] == password):
        return jsonify(usuario)
    
    return jsonify({"mensaje": "Credenciales incorrectas"}), 401

@app.route('/register',methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    crear_usuario(name,email,password)
    return jsonify({"mensaje":"Bienvenido nuevo Usuario!"}), 200

@app.route('/createconf',methods=['POST'])
def new_conf():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    fecha = data.get('fecha')
    hora = data.get('hora')
    duracion = data.get('duracion')
    usuario = buscar_usuarios(email)
    print(usuario[3])
    if(not(usuario[3] == password)):
        return jsonify({"mensaje":"Usuario no registrado"}), 401  
    crear_videoconferencia(fecha,hora,duracion,usuario[0])
    return jsonify({"mensaje":"Conferencia creada exitosamente"}), 201

@app.route('/aggmeet',methods=['POST'])
def aggmeet():
    data = request.json
    usuario_id = data.get('usuario_id')
    videoconferencia_id = data.get('videoconferencia_id')
    agregar_participante(usuario_id, videoconferencia_id)
    return jsonify({"mensaje":"Parcitipante agregado a la reunion"}), 401

@app.route('/meetppl', methods=['GET'])
def meetppl():
    data = request.json
    videoconferencia_id = data.get('videoconferencia_id')
    resultados = obtener_participantes(videoconferencia_id)
    
    return jsonify(resultados), 401

@app.route('/delppl', methods=['DELETE'])
def delppl():
    data = request.json
    videoconferencia_id = data.get('videoconferencia_id')
    usuario_id = data.get('usuario_id')
    resultados = eliminar_participante(usuario_id, videoconferencia_id)
    
    return jsonify({"mensaje":"El usuario ha sido borrado exitosamente de la reunion"}), 401

@app.route('/delmeet',methods=['DELETE'])
def delmeet():
    data = request.json
    videoconferencia_id = data.get('videoconferencia_id')
    eliminar_meet(videoconferencia_id)
    
    return jsonify({"mensaje":"Reunion eliminada"}), 401

@app.route('/updatemeet',methods=['POST'])
def updatemeet():
    data = request.json
    videoconferencia_id = data.get('videoconferencia_id')
    fecha = data.get('fecha')
    
    
    actualizar_videoconferencia(fecha,videoconferencia_id)
    return jsonify({"mensaje":"Reunion actualizada con exito"}), 201

# # Ruta para agregar usuarios (POST)
# @app.route('/agregar_usuario', methods=['POST'])
# def agregar_usuario():
#     nuevo_usuario = {
#         "id": len(usuarios) + 1,
#         "nombre": request.json.get('nombre'),
#         "contrasena": request.json.get('contrasena')
#     }

#     usuarios.append(nuevo_usuario)

#     return jsonify({"mensaje": "Usuario agregado exitosamente", "usuario_id": nuevo_usuario['id']}), 201
# @app.route('/register', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         name = request.form['name']
#         error = None

#         if not email:
#             error = 'Username is required.'
#         elif not password:
#             error = 'Password is required.'

#         if error is None:
#             crear_usuario(name,email,password)

#     return render_template('register.html')
# @app.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         usuario = buscar_usuarios(email)
#         if(usuario[0][3] == password):
#             session.clear()
#             session['user_id'] = usuario[0][0]
#             return redirect(url_for('login'))
            
#     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
