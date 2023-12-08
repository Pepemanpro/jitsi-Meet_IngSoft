#CrudBD_Usuarios.py
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="jitsi_meet_db"
    )


def cerrar_conexion(conexion, cursor):
    cursor.close()
    conexion.close()

def crear_usuario(nombre, correo, contrasena, foto_perfil=None, estado=None, preferencias=None):
    conexion = conectar()
    cursor = conexion.cursor()

    insertar_usuario = "INSERT INTO Usuarios (nombre, correo, contrasena, foto_perfil, estado, preferencias) VALUES (%s, %s, %s, %s, %s, %s)"
    datos_usuario = (nombre, correo, contrasena, foto_perfil, estado, preferencias)
    cursor.execute(insertar_usuario, datos_usuario)
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def leer_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()

    seleccionar_usuarios = "SELECT * FROM Usuarios"
    cursor.execute(seleccionar_usuarios)
    resultados = cursor.fetchall()

    cerrar_conexion(conexion, cursor)
    return resultados

def buscar_usuarios(correo):
    conexion = conectar()
    cursor=conexion.cursor()
    query = "SELECT * FROM Usuarios WHERE correo = %s"
    cursor.execute(query, (correo,))
    results = cursor.fetchall()
    print(results)
    cerrar_conexion(conexion,cursor)
    return results[0]

def actualizar_usuario(usuario_id, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    actualizar_usuario = "UPDATE Usuarios SET nombre = %s WHERE id = %s"
    cursor.execute(actualizar_usuario, (nuevo_nombre, usuario_id))
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def eliminar_usuario(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()

    eliminar_usuario = "DELETE FROM Usuarios WHERE id = %s"
    cursor.execute(eliminar_usuario, (usuario_id,))
    conexion.commit()

    cerrar_conexion(conexion, cursor)
