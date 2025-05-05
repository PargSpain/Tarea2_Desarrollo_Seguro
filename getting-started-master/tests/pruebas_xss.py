from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obtener_subcarpetas(url_principal):
    """
    Obtiene todas las subcarpetas de una URL principal.

    Args:
        url_principal: La URL principal de la que se quieren obtener las subcarpetas.

    Returns:
        Una lista de URLs de subcarpetas.
    """
    subcarpetas = []
    try:
        respuesta = requests.get(url_principal)
        respuesta.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        enlaces = soup.find_all('a')
        for enlace in enlaces:
            href = enlace.get('href')
            if href:
                url_completa = urljoin(url_principal, href)
                # Añadir condición para que no se repitan las subcarpetas y que no se salgan del dominio
                if url_completa.startswith(url_principal) and url_completa not in subcarpetas:
                  subcarpetas.append(url_completa)
        return subcarpetas
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las subcarpetas de {url_principal}: {e}")
        return []

def probar_xss(driver, url, entradas_id, codigo_xss):
    """
    Prueba si una URL es vulnerable a XSS inyectando código malicioso en múltiples campos de entrada.

    Args:
        driver: El objeto webdriver de Selenium.
        url: La URL de la página a probar.
        entradas_id: Una lista de los IDs de los elementos de entrada (ej., ["title", "description"]).
        codigo_xss: El código HTML/JavaScript malicioso a inyectar.
    """
    driver.get(url)
    print(f"Probando XSS en la URL: {url}")
    hubo_xss = False  # Variable para rastrear si se detectó XSS en la página

    for entrada_id in entradas_id:
        try:
            entrada = driver.find_element(By.ID, entrada_id)
            entrada.send_keys(codigo_xss)
            entrada.submit()
            time.sleep(2)  # Esperar a que se cargue la página
            try:
                alerta = driver.switch_to.alert
                print(f"  XSS detectado en el campo: {entrada_id}")
                alerta.accept()  # Aceptar la alerta para que la prueba continúe
                hubo_xss = True
            except:
                print(f"  No se detectó XSS en el campo: {entrada_id}")
        except NoSuchElementException:
            print(f"  No se encontró el campo: {entrada_id} en esta página")

    if hubo_xss:
        print(f"  ¡Se detectó XSS en la página: {url}!")
        return True
    else:
        print(f"  No se detectó XSS en la página: {url}")
        return False


if __name__ == "__main__":
    # Configuración del navegador (ejemplo con Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless (sin interfaz gráfica)
    driver = webdriver.Chrome(options=chrome_options)  # Asegúrate de que tienes chromedriver instalado y en el PATH

    # URL principal
    url_principal = "http://localhost:8000/"  # Reemplaza con la URL de tu aplicación

    # Obtener todas las subcarpetas
    urls_a_probar = obtener_subcarpetas(url_principal)
    if not urls_a_probar:
        print(f"No se encontraron subcarpetas en {url_principal}. Probando solo la URL principal.")
        urls_a_probar = [url_principal]

    # Lista de campos de entrada a probar en cada página
    campos_a_probar = ["title", "description"]  # Campos comunes

    # Código XSS a inyectar
    codigo_xss = "<script>alert('XSS')</script>"

    for url in urls_a_probar:
        probar_xss(driver, url, campos_a_probar, codigo_xss)

    driver.quit()
