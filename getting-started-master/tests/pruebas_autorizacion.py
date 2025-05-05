import requests

def probar_autorizacion(url, usuario, contrasena, url_esperada):
    """
    Prueba si un usuario puede acceder a una URL protegida.

    Args:
        url: La URL a la que se intenta acceder.
        usuario: El nombre de usuario para la autenticación.
        contrasena: La contraseña para la autenticación.
        url_esperada: La URL a la que se debería redirigir si la autorización es exitosa.
    """
    sesion = requests.Session()
    # Primero, obtener el token CSRF (si la aplicación lo usa)
    respuesta_login = sesion.get(url)
    # print(respuesta_login.text) #Descomentar si necesitas ver el HTML para encontrar el token
    token_csrf = "" # Reemplazar con la lógica para extraer el token CSRF del HTML
    if token_csrf:
      formulario_login = {
          'username': usuario,
          'password': contrasena,
          'csrf_token': token_csrf # Añadir el token al formulario
      }
    else:
       formulario_login = {
          'username': usuario,
          'password': contrasena,
      }
    # Enviar la petición de inicio de sesión
    respuesta_login = sesion.post(url, data=formulario_login)

    # Intentar acceder a la URL protegida
    respuesta = sesion.get(url_esperada)

    if url_esperada in respuesta.url:
        print(f"Autorización exitosa para {usuario} en {url_esperada}")
        return True
    else:
        print(f"Autorización fallida para {usuario} en {url_esperada}.  Obtenido: {respuesta.url}")
        return False

if __name__ == "__main__":
    # Ejemplo: Probar acceso de un usuario normal a una ruta de administrador
    url_login = "http://localhost:8000/login"  # Reemplazar
    url_admin = "http://localhost:8000/admin"  # Reemplazar
    probar_autorizacion(url_login, "usuario_normal", "contrasena_normal", url_admin)

    # Ejemplo: Probar acceso de un administrador a una ruta de administrador
    probar_autorizacion(url_login, "administrador", "contrasena_administrador", url_admin)
