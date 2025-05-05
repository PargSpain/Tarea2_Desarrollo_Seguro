import docker  # Importar la librería de Docker para Python
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_version_aplicacion():
    """
    Obtiene la versión de la aplicación To Do utilizando la librería de Docker para Python.

    Returns:
        str: La versión de la aplicación, o None si no se puede obtener.
    """
    try:
        client = docker.from_env()
        # Asegúrate de que el nombre del contenedor es correcto
        container = client.containers.get('getting-started')  
        imagen = container.image
        # La versión puede estar en el tag de la imagen, por ejemplo.
        if imagen.tags:
            version = imagen.tags[0].split(':')[-1]
            logging.info(f"Versión de la aplicación To Do obtenida: {version}")
            return version
        else:
            logging.warning("La imagen del contenedor no tiene tags. No se puede obtener la versión.")
            return None
    except docker.errors.NotFound as e:
        logging.error(f"Error: No se encontró el contenedor 'getting-started': {e}")
        return None
    except docker.errors.APIError as e:
        logging.error(f"Error de la API de Docker: {e}")
        return None
    except Exception as e:
        logging.error(f"Error inesperado al obtener la versión: {e}")
        return None
    
# Ejemplo de uso (puedes descomentar esto para probar la función)
if __name__ == "__main__":
    version = obtener_version_aplicacion()
    if version:
        print(f"Versión de la aplicación: {version}")
    else:
        print("No se pudo obtener la versión de la aplicación.")
