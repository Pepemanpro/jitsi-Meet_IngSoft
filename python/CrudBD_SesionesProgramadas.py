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

def crear_sesion_programada(fecha, hora, creador_id):
    conexion = conectar()
    cursor = conexion.cursor()

    insertar_sesion = "INSERT INTO SesionesProgramadas (fecha, hora, creador_id) VALUES (%s, %s, %s)"
    datos_sesion = (fecha, hora, creador_id)
    cursor.execute(insertar_sesion, datos_sesion)
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def leer_sesiones_programadas():
    conexion = conectar()
    cursor = conexion.cursor()

    seleccionar_sesiones = "SELECT * FROM SesionesProgramadas"
    cursor.execute(seleccionar_sesiones)
    resultados = cursor.fetchall()

    cerrar_conexion(conexion, cursor)
    return resultados

def actualizar_sesion_programada(sesion_id, nueva_fecha):
    conexion = conectar()
    cursor = conexion.cursor()

    actualizar_sesion = "UPDATE SesionesProgramadas SET fecha = %s WHERE id = %s"
    cursor.execute(actualizar_sesion, (nueva_fecha, sesion_id))
    conexion.commit()

    cerrar_conexion(conexion, cursor)

def eliminar_sesion_programada(sesion_id):
    conexion = conectar()
    cursor = conexion.cursor()

    eliminar_sesion = "DELETE FROM SesionesProgramadas WHERE id = %s"
    cursor.execute(eliminar_sesion, (sesion_id,))
    conexion.commit()

    cerrar_conexion(conexion, cursor)