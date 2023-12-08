from CrudBD_Usuarios import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario
from CrudBD_Videoconferencias import crear_videoconferencia, leer_videoconferencias, actualizar_videoconferencia, eliminar_videoconferencia
from CrudBD_Participantes import agregar_participante, obtener_participantes
from CrudBD_SesionesProgramadas import crear_sesion_programada, leer_sesiones_programadas, actualizar_sesion_programada, eliminar_sesion_programada

# Crear algunos usuarios
crear_usuario("Usuario1", "usuario1@example.com", "contrasena1", "foto1.jpg", "Activo", "Preferencias1")
crear_usuario("Usuario2", "usuario2@example.com", "contrasena2", "foto2.jpg", "Inactivo", "Preferencias2")

# Leer todos los usuarios
print("Usuarios existentes:")
usuarios = leer_usuarios()
for usuario in usuarios:
    print(usuario)

# Actualizar un usuario
actualizar_usuario(1, "NuevoNombreUsuario")

# Crear algunas videoconferencias
crear_videoconferencia("2023-12-05", "15:00:00", 60, 1)
crear_videoconferencia("2023-12-10", "18:30:00", 45, 2)

# Leer todas las videoconferencias
print("\nVideoconferencias existentes:")
videoconferencias = leer_videoconferencias()
for videoconferencia in videoconferencias:
    print(videoconferencia)

# Actualizar una videoconferencia
actualizar_videoconferencia(1, "2023-12-12")

# Agregar participantes a una videoconferencia
agregar_participante(1, 1)
agregar_participante(2, 1)

# Obtener participantes de una videoconferencia
print("\nParticipantes de la videoconferencia 1:")
participantes = obtener_participantes()
for participante in participantes:
    print(participante)

# Crear algunas sesiones programadas
crear_sesion_programada("2023-12-05", "15:00:00", 1)
crear_sesion_programada("2023-12-10", "18:30:00", 2)

# Leer todas las sesiones programadas
print("\nSesiones programadas existentes:")
sesiones_programadas = leer_sesiones_programadas()
for sesion_programada in sesiones_programadas:
    print(sesion_programada)

# Actualizar una sesión programada
actualizar_sesion_programada(1, "2023-12-12")

# Eliminar una sesión programada
eliminar_sesion_programada(2)

# # Eliminar un usuario
# eliminar_usuario(2)

# # Eliminar una videoconferencia
# eliminar_videoconferencia(2)
