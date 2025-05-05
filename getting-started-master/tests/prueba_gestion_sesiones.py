import requests
import time
import uuid

# URL de la aplicación web que quieres probar
BASE_URL = "http://localhost:8000/tutorial/"

# Rutas de la aplicación (ajusta según sea necesario)
#LOGIN_URL = f"{BASE_URL}/login"
#LOGOUT_URL = f"{BASE_URL}/logout"
PROFILE_URL = f"{BASE_URL}/profile"
SESSION_TIMEOUT_URL = f"{BASE_URL}/session_timeout" # Ruta para probar el timeout de sesión

# Credenciales de un usuario de prueba
USERNAME = "admin"
PASSWORD = "pass"

# Tiempo de espera para las pruebas de timeout de sesión (en segundos)
SESSION_TIMEOUT = 10 # Un valor pequeño para las pruebas, ¡aumenta en producción!

def test_login_logout():
    """
    Prueba el inicio y cierre de sesión básico.
    """
    print("\n[PRUEBA] Inicio y cierre de sesión")
    session = requests.Session()

    # Intenta iniciar sesión
    login_data = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, data=login_data)
    assert response.status_code == 200, f"Error al iniciar sesión: {response.status_code}"
    print("  [PASSED] Inicio de sesión exitoso")

    # Verifica que la sesión esté activa (por ejemplo, accediendo a un perfil)
    response = session.get(PROFILE_URL)
    assert response.status_code == 200, f"Error al acceder al perfil: {response.status_code}"
    print("  [PASSED] Sesión activa verificada")

    # Cierra la sesión
    response = session.get(LOGOUT_URL) # o session.post(LOGOUT_URL), dependiendo de tu app
    assert response.status_code == 200, f"Error al cerrar sesión: {response.status_code}"
    print("  [PASSED] Cierre de sesión exitoso")

    # Verifica que la sesión se haya cerrado
    response = session.get(PROFILE_URL)
    assert response.status_code != 200, f"Error: ¡La sesión no se cerró correctamente! Código: {response.status_code}" #Comprueba que el codigo no sea 200
    print("  [PASSED] Sesión cerrada verificada")
    return session # Devuelve la sesión para usarla en otras pruebas si es necesario


def test_invalid_login():
    """
    Prueba el inicio de sesión con credenciales inválidas.
    """
    print("\n[PRUEBA] Inicio de sesión inválido")
    session = requests.Session()
    login_data = {"username": USERNAME, "password": "wrong_password"}
    response = session.post(LOGIN_URL, data=login_data)
    assert response.status_code != 200, f"Error: ¡Inicio de sesión inválido exitoso! Código: {response.status_code}" #Comprueba que el codigo no sea 200
    print("  [PASSED] Inicio de sesión inválido rechazado")

def test_session_hijacking():
    """
    Prueba la resistencia al secuestro de sesión.
    """
    print("\n[PRUEBA] Secuestro de sesión")
    session1 = requests.Session()
    login_data = {"username": USERNAME, "password": PASSWORD}
    response = session1.post(LOGIN_URL, data=login_data)
    assert response.status_code == 200, "Error al iniciar sesión para la sesión 1"
    session_cookie = session1.cookies.get_dict() #Guarda las cookies de la sesión

    session2 = requests.Session()
    # Intenta usar las cookies de la sesión1 en la sesión2
    session2.cookies.update(session_cookie)
    response = session2.get(PROFILE_URL)
    # Aquí, la aserción depende de cómo tu aplicación maneja el secuestro de sesión.
    # Puede que la aplicación redirija a la página de inicio de sesión, o que muestre un error.
    # Ajusta la aserción según el comportamiento esperado.
    assert response.status_code != 200, f"Error: ¡Secuestro de sesión posible! Código: {response.status_code}"
    print("  [PASSED] Secuestro de sesión prevenido (o manejado)")



def test_session_timeout():
    """
    Prueba el timeout de la sesión.
    """
    print("\n[PRUEBA] Timeout de sesión")
    session = requests.Session()
    login_data = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, data=login_data)
    assert response.status_code == 200, "Error al iniciar sesión"

    print(f"  [INFO] Esperando {SESSION_TIMEOUT} segundos para el timeout de sesión...")
    time.sleep(SESSION_TIMEOUT) # Espera el timeout

    response = session.get(PROFILE_URL)
    assert response.status_code != 200, f"Error: ¡La sesión no expiró! Código: {response.status_code}"
    print("  [PASSED] Sesión expiró correctamente")



def test_session_fixation():
    """
    Prueba la vulnerabilidad a la fijación de sesión.
    """
    print("\n[PRUEBA] Fijación de sesión")
    session = requests.Session()
    initial_session_id = session.cookies.get_dict().get('sessionid', None) #Obtiene el ID de la sesion

    # Simula un inicio de sesión
    login_data = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, data=login_data)
    assert response.status_code == 200, "Error al iniciar sesión"

    #Obtiene el nuevo ID de sesión después del inicio.
    new_session_id = session.cookies.get_dict().get('sessionid', None)
    assert new_session_id != initial_session_id, "Error: ¡La sesión no se regeneró!"
    print("  [PASSED] Fijación de sesión prevenida")


def test_concurrent_sessions():
    """
    Prueba el manejo de sesiones concurrentes (múltiples inicios de sesión con el mismo usuario).
    """
    print("\n[PRUEBA] Sesiones concurrentes")
    session1 = requests.Session()
    login_data = {"username": USERNAME, "password": PASSWORD}
    response1 = session1.post(LOGIN_URL, data=login_data)
    assert response1.status_code == 200, "Error al iniciar sesión en la sesión 1"

    session2 = requests.Session()
    response2 = session2.post(LOGIN_URL, data=login_data)
    assert response2.status_code == 200, "Error al iniciar sesión en la sesión 2"
    # La prueba pasa si el servidor no devuelve error, habría que comprobar el comportamiento deseado
    print("  [PASSED] Sesiones concurrentes manejadas") #Añadido mensaje


if __name__ == "__main__":
    # Ejecuta las pruebas
    test_login_logout()
    test_invalid_login()
    test_session_hijacking()
    test_session_timeout()
    test_session_fixation()
    test_concurrent_sessions()
    print("\n[INFO] Todas las pruebas completadas")