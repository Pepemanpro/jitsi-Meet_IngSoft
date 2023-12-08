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

def agregar_participante(usuario_id, videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    insertar_participante = "INSERT INTO Participantes (usuario_id, videoconferencia_id) VALUES (%s, %s)"
    datos_participante = (usuario_id, videoconferencia_id)
    cursor.execute(insertar_participante, datos_participante)
    conexion.commit()

    cerrar_conexion(conexion, cursor)
    

def obtener_participantes(videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    seleccionar_participantes = "SELECT usuario_id FROM Participantes WHERE videoconferencia_id = %s"
    cursor.execute(seleccionar_participantes,(videoconferencia_id,))
    resultados = cursor.fetchall()

    cerrar_conexion(conexion, cursor)
    return resultados

def eliminar_participante(usuario_id, videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    eliminar_participante = "DELETE FROM Participantes WHERE usuario_id = %s AND videoconferencia_id = %s"
    cursor.execute(eliminar_participante, (usuario_id, videoconferencia_id))
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def eliminar_meet(videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    eliminar_participante = "DELETE FROM Participantes WHERE videoconferencia_id = %s"
    cursor.execute(eliminar_participante, (videoconferencia_id,))
    conexion.commit()

    cerrar_conexion(conexion, cursor)