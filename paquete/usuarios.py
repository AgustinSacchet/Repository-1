usuarios={}

def regristrar_usuario():
  nombre=input("Ingrese nombre de usuario: ")
  contraseña=input("Ingrese contraseña: ")
  if nombre in usuarios:
    print("El usuario ya esta registrado!")
  else:
    usuarios[nombre]=contraseña
    print("Usuario registrado con exito.")

def leer_usuarios(usuarios):
  for nombre_usuario, contraseña in usuarios.items():
    print(f"Nombre de usuario: {nombre_usuario} / Contraseña: {contraseña}")

def iniciar_sesion(nombre,contraseña):
  if nombre in usuarios:
    if usuarios[nombre]==contraseña:
      print("Inicio de sesion exitoso.")
    else:
      print("Contraseña incorrecta, intente nuevamente!")
  else:
    print("Usuario incorrecto, intente nuevamente!")