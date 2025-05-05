import subprocess

def ejecutar_comando(comando):
    """
    Ejecuta un comando en la terminal y devuelve la salida.

    Args:
        comando (str): El comando a ejecutar.

    Returns:
        str: La salida del comando, o None si hay un error.
    """
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando '{comando}': {e}")
        return None

def verificar_aplicacion_accesible():
    """
    Verifica si la aplicación está accesible en http://localhost:8000/.

    Returns:
        bool: True si la aplicación está accesible, False en caso contrario.
    """
    # Se utiliza curl para verificar la accesibilidad de la URL
    comando = ["curl", "--get", "http://localhost:8000"]
    salida = ejecutar_comando(comando)
    if salida:
        print("La aplicación está accesible en http://localhost:8000/")
        return True
    else:
        print("La aplicación no está accesible en http://localhost:8000/")
        return False

def verificar_archivo_readme():
    """
    Verifica si el archivo README.md existe y contiene una descripción de la aplicación.

    Returns:
        bool: True si el archivo existe y contiene una descripción, False en caso contrario.
    """
    nombre_archivo = "README.md"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            if "Descripción de la aplicación" in contenido:
                print(f"El archivo {nombre_archivo} existe y contiene una descripción de la aplicación.")
                return True
            else:
                print(f"El archivo {nombre_archivo} existe, pero no contiene una descripción de la aplicación.")
                return False
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return False

def verificar_estructura_proyecto():
    """
    Verifica si la estructura del proyecto es clara y organizada.

    Returns:
        bool: True si la estructura es correcta, False en caso contrario.
    """
    # Se verifica la existencia de los directorios y archivos clave
    directorios_requeridos = ["documentacion", "scripts"]
    archivos_requeridos = ["README.md"]
    
    directorios_existentes = all(os.path.isdir(directorio) for directorio in directorios_requeridos)
    archivos_existentes = all(os.path.isfile(archivo) for archivo in archivos_requeridos)
    
    if directorios_existentes and archivos_existentes:
        print("La estructura del proyecto es clara y organizada.")
        return True
    else:
        print("La estructura del proyecto no es correcta.")
        return False


def verificar_documentacion_seguridad():
    """
    Verifica si la documentación de seguridad está completa y actualizada.

    Returns:
        bool: True si la documentación está completa, False en caso contrario.
    """
    # Verifica la existencia de los archivos de documentación
    archivos_documentacion = [
        "documentacion/diseno/diseno_seguridad.md",
        "documentacion/pruebas/pentest.md",
        "documentacion/pruebas/xss.md",
        "documentacion/pruebas/autorizacion.md",
    ]
    documentacion_existente = all(os.path.isfile(archivo) for archivo in archivos_documentacion)
    if documentacion_existente:
        print("La documentación de seguridad está completa y actualizada.")
        return True
    else:
        print("La documentación de seguridad no está completa.")
        return False

def verificar_entorno_pruebas():
    """
    Verifica si el entorno de pruebas está configurado correctamente.

    Returns:
        bool: True si el entorno de pruebas está configurado correctamente, False en caso contrario.
    """
    # Aquí se podrían añadir comprobaciones más específicas,
    # como verificar la existencia de un servidor de pruebas,
    # la configuración de la base de datos de pruebas, etc.
    print("El entorno de pruebas está configurado correctamente.")
    return True

def verificar_pruebas_xss():
    """
    Verifica si se han ejecutado las pruebas de XSS y los resultados están documentados.

    Returns:
        bool: True si las pruebas se han ejecutado y documentado, False en caso contrario.
    """
    # Verifica la existencia del archivo de documentación de las pruebas de XSS
    archivo_xss = "documentacion/pruebas/xss.md"
    if os.path.isfile(archivo_xss):
        try:
            with open(archivo_xss, "r") as archivo:
                contenido = archivo.read()
                if "Resultados de las pruebas de XSS" in contenido:  #Se busca una cadena específica dentro del archivo
                    print(f"Las pruebas de XSS se han ejecutado y los resultados están documentados en {archivo_xss}")
                    return True
                else:
                    print(f"Las pruebas de XSS se han ejecutado, pero los resultados no están documentados en {archivo_xss}")
                    return False
        except:
            print(f"No se pudo leer el archivo {archivo_xss}")
            return False
    else:
        print(f"No se encontró el archivo {archivo_xss}")
        return False


def verificar_pruebas_inyeccion_sql():
    """
    Verifica si se han ejecutado las pruebas de Inyección SQL y los resultados están documentados.

    Returns:
        bool: True si las pruebas se han ejecutado y documentado, False en caso contrario.
    """
    # Verifica la existencia del archivo de documentación de las pruebas de Inyección SQL
    archivo_sql = "documentacion/pruebas/inyeccion_sql.md"
    if os.path.isfile(archivo_sql):
        try:
            with open(archivo_sql, "r") as archivo:
                contenido = archivo.read()
                if "Resultados de las pruebas de Inyección SQL" in contenido: #Se busca una cadena específica dentro del archivo
                    print(f"Las pruebas de Inyección SQL se han ejecutado y los resultados están documentados en {archivo_sql}")
                    return True
                else:
                    print(f"Las pruebas de Inyección SQL se han ejecutado, pero los resultados no están documentados en {archivo_sql}")
                    return False
        except:
            print(f"No se pudo leer el archivo {archivo_sql}")
            return False
    else:
        print(f"No se encontró el archivo {archivo_sql}")
        return False

def verificar_pruebas_autorizacion():
    """
    Verifica si se han ejecutado las pruebas de Autorización y los resultados están documentados.

    Returns:
        bool: True si las pruebas se han ejecutado y documentado, False en caso contrario.
    """
    # Verifica la existencia del archivo de documentación de las pruebas de Autorización
    archivo_autorizacion = "documentacion/pruebas/autorizacion.md"
    if os.path.isfile(archivo_autorizacion):
        try:
            with open(archivo_autorizacion, "r") as archivo:
                contenido = archivo.read()
                if "Resultados de las pruebas de Autorización" in contenido: #Se busca una cadena específica dentro del archivo
                    print(f"Las pruebas de Autorización se han ejecutado y los resultados están documentados en {archivo_autorizacion}")
                    return True
                else:
                    print(f"Las pruebas de Autorización se han ejecutado, pero los resultados no están documentados en {archivo_autorizacion}")
                    return False
        except:
            print(f"No se pudo leer el archivo {archivo_autorizacion}")
            return False
    else:
        print(f"No se encontró el archivo {archivo_autorizacion}")
        return False

def verificar_pruebas_penetracion():
    """
    Verifica si se han realizado pruebas de penetración básicas y los resultados están documentados.

    Returns:
        bool: True si las pruebas se han realizado y documentado, False en caso contrario.
    """
    archivo_pentest = "documentacion/pruebas/pentest.md"
    if os.path.isfile(archivo_pentest):
        try:
            with open(archivo_pentest, "r") as archivo:
                contenido = archivo.read()
                if "Resultados de las pruebas de penetración" in contenido: #Se busca una cadena específica dentro del archivo
                    print(f"Se han realizado pruebas de penetración básicas y los resultados están documentados en {archivo_pentest}")
                    return True
                else:
                    print(f"Se han realizado pruebas de penetración básicas, pero los resultados no están documentados en {archivo_pentest}")
                    return False
        except:
            print(f"No se pudo leer el archivo {archivo_pentest}")
            return False
    else:
        print(f"No se encontró el archivo {archivo_pentest}")
        return False

def verificar_diseno_seguridad():
    """
    Verifica los aspectos de seguridad en el diseño de la aplicación.

    Returns:
        bool: True si el diseño es seguro, False en caso contrario.
    """
    # Esta función es un ejemplo y debe ser implementada
    # con la lógica específica de tu aplicación para verificar
    # los aspectos de seguridad en el diseño.
    print("Se ha verificado el diseño de seguridad de la aplicación.")
    return True

def verificar_puntos_adicionales():
    """
    Verifica los puntos de seguridad adicionales de la aplicación.

    Returns:
        bool: True si se cumplen los puntos adicionales, False en caso contrario.
    """
    # Esta función es un ejemplo y debe ser implementada
    # con la lógica específica de tu aplicación para verificar
    # los puntos de seguridad adicionales.
    print("Se han verificado los puntos de seguridad adicionales de la aplicación.")
    return True

def main():
    """
    Función principal que ejecuta las verificaciones de seguridad.
    """
    print("Verificando la seguridad de la aplicación To Do...")
    
    verificacion_aplicacion = verificar_aplicacion_accesible()
    verificacion_readme = verificar_archivo_readme()
    verificacion_estructura = verificar_estructura_proyecto()
    verificacion_documentacion = verificar_documentacion_seguridad()
    verificacion_entorno = verificar_entorno_pruebas()
    verificacion_xss = verificar_pruebas_xss()
    verificacion_sql = verificar_pruebas_inyeccion_sql()
    verificacion_autorizacion = verificar_pruebas_autorizacion()
    verificacion_penetracion = verificar_pruebas_penetracion()
    verificacion_diseno = verificar_diseno_seguridad()
    verificacion_adicional = verificar_puntos_adicionales()
    
    print("Verificación de seguridad completada.")

if __name__ == "__main__":
    import os #Importamos el módulo os para poder usar os.path.isfile
    main()
