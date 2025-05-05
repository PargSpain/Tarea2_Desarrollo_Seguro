import zapv2
import time

def run_zap_scan(target_url, api_key):
    """
    Ejecuta un escaneo de seguridad con OWASP ZAP.

    Args:
        target_url (str): La URL de la aplicación a escanear.
        api_key (str): La API key de ZAP.
    """
    zap = zapv2.ZAPv2(
        apikey=api_key,
        proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
    )  # ZAP proxy por defecto
    print(f'Escaneando {target_url}')

    zap.spider.scan(target_url)  # Iniciar el rastreo
    while int(zap.spider.status) < 100:
        print(f'Progreso del rastreo: {zap.spider.status}%')
        time.sleep(5)

    print('Rastreo completado')

    zap.ascan.scan(target_url)  # Iniciar el escaneo activo
    while int(zap.ascan.status) < 100:
        print(f'Progreso del escaneo: {zap.ascan.status}%')
        time.sleep(5)

    print('Escaneo activo completado')

    alerts = zap.core.alerts()  # Obtener las alertas
    if alerts:
        print('Alertas encontradas:')
        for alert in alerts:
            print(
                f'[{alert["risk"]}][{alert["confidence"]}] {alert["name"]}: {alert["url"]}'
            )
            print(f'Descripción: {alert["description"]}')
            print(f'Solución: {alert["solution"]}')
    else:
        print('No se encontraron alertas')

if __name__ == "__main__":
    target_url = 'http://localhost:8000'  # Reemplazar
    api_key = 'tu_api_key'  # Reemplazar con tu API key de ZAP
    run_zap_scan(target_url, api_key)
