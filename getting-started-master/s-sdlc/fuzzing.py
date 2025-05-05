import requests

def fuzz_api(url, payloads):
    """
    Realiza fuzzing en la API de la aplicación To Do.

    Args:
        url (str): La URL base de la API.
        payloads (list): Una lista de payloads maliciosos.
    """
    anomalies_found = 0  # Contador de anomalías encontradas
    anomalies_locations = [] # Lista para guardar la información de las anomalías
    for payload in payloads:
        try:
            data = {'title': payload, 'description': 'Fuzzing test'}  # Adaptar los parámetros de la API
            response = requests.post(f"{url}/tasks", json=data)  # Endpoint de ejemplo
            if response.status_code != 201:  # Código de éxito para la creación
                print(f"Anomalía detectada con payload: {payload}")
                print(f"Código de estado: {response.status_code}")
                print(f"Respuesta: {response.text}")
                anomalies_found += 1
                anomalies_locations.append(f"Payload: {payload}, URL: {url}/tasks") # Añade detalles de la anomalía
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar payload: {payload} - {e}")
            anomalies_found += 1
            anomalies_locations.append(f"Payload: {payload}, Error: {e}") # Añade detalles del error
    return anomalies_found, anomalies_locations

if __name__ == "__main__":
    api_url = "http://localhost:8000"  # Reemplazar con la URL de tu API
    fuzz_payloads = [
        "' OR 1=1 --",  # Inyección SQL
        "<script>alert('XSS')</script>",  # XSS
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  # Overflow de buffer
    ]
    num_anomalies, anomaly_locations = fuzz_api(api_url, fuzz_payloads) # Guarda el número y la ubicación de anomalías
    if num_anomalies > 0:
        print(f"Fuzzing completado. Se encontraron {num_anomalies} anomalías en los siguientes lugares:")
        for location in anomaly_locations:
            print(f"- {location}") # Imprime cada ubicación de anomalía
    else:
        print("Fuzzing completado. No se encontraron anomalías.")


  
