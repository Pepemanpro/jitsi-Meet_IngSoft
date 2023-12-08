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

def crear_videoconferencia(fecha, hora, duracion, creador_id):
    conexion = conectar()
    cursor = conexion.cursor()

    insertar_videoconferencia = "INSERT INTO Videoconferencias (fecha, hora, duracion, creador_id) VALUES (%s, %s, %s, %s)"
    datos_videoconferencia = (fecha, hora, duracion, creador_id)
    cursor.execute(insertar_videoconferencia, datos_videoconferencia)
    conexion.commit()
    
    cerrar_conexion(conexion, cursor)
    

def leer_videoconferencias():
    conexion = conectar()
    cursor = conexion.cursor()

    seleccionar_videoconferencias = "SELECT * FROM Videoconferencias"
    cursor.execute(seleccionar_videoconferencias)
    resultados = cursor.fetchall()

    cerrar_conexion(conexion, cursor)
    return resultados

def actualizar_videoconferencia(nueva_fecha, videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    actualizar_videoconferencia = "UPDATE Videoconferencias SET fecha = %s WHERE id = %s"
    cursor.execute(actualizar_videoconferencia, (nueva_fecha, videoconferencia_id))
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def eliminar_videoconferencia(videoconferencia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    eliminar_videoconferencia = "DELETE FROM Videoconferencias WHERE id = %s"
    cursor.execute(eliminar_videoconferencia, (videoconferencia_id,))
    conexion.commit()

    cerrar_conexion(conexion, cursor)
