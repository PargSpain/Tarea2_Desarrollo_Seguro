# cano_martin_ngueyou
El presente repositorio se ha creado con fines educativos para una tarea de la asignatura de Desarrollo Seguro.
# Aplicación To Do con Docker y SDLC Seguro

# Autores:
 - Francisco Javier Cano Sánchez
 - Neil Lonely Ngueyou Simo
 - Mario Martín Peredo
 - https://github.com/PargSpain/cano_martin_ngueyou

## Descripción

El presente repositorio se ha creado con fines educativos para una tarea de la asignatura de Desarrollo Seguro.
Esta es una aplicación web para gestionar tareas To Do. La aplicación está containerizada con Docker para facilitar su despliegue y ejecución. Se ha desarrollado siguiendo un SDLC seguro para integrar consideraciones de seguridad en cada etapa del desarrollo.

La aplicación se ejecuta localmente en Windows 11 utilizando Docker Desktop y está accesible en el puerto 8000.

## Cómo Ejecutar la Aplicación

1.  Asegúrate de tener Docker Desktop instalado.
2.  Clona este repositorio:
    ```bash
    git clone <URL_de_tu_repositorio>
    ```
3.  Navega al directorio del proyecto:
    ```bash
    cd proyecto_to_do_docker
    ```
4.  Construye la imagen de Docker (si no la has construido ya):
    ```bash
    docker build -t todo-app .
    ```
5.  Ejecuta el contenedor de Docker:
    ```bash
    docker run -p 8000:8000 todo-app
    ```
6.  Abre tu navegador web y accede a `http://localhost:8000` para ver la aplicación.

# ## Para Windows:

### Pasos

El principal cambio al pasar de Linux a Windows 11 está en los comandos que se utilizan en la terminal. Mientras que Linux utiliza comandos como `bash`, `chmod`, y `./`, en Windows se utiliza el Símbolo del sistema (cmd) o PowerShell, con comandos diferentes.

## 1. Configuración Inicial

* **Docker Desktop:** Asegúrate de tener Docker Desktop instalado y en ejecución en tu Windows 11. Puedes descargarlo desde la página oficial de Docker (https://www.docker.com/products/docker-desktop/).

* **Acceso a la Terminal:** Abre el Símbolo del sistema (cmd) o PowerShell como administrador. Esto es importante para ejecutar comandos que requieran privilegios elevados.

## 2. Creación de la Imagen Docker

Los pasos para crear la imagen Docker son similares a los de Linux, pero con algunas adaptaciones en los comandos:

* **Navegar al directorio:** Utiliza el comando `cd` para cambiar al directorio donde se encuentra tu `Dockerfile`. Por ejemplo:

    ```
    cd C:\ruta\al\proyecto\aplicacion
    ```

* **Construir la imagen:** Ejecuta el siguiente comando para construir la imagen Docker:

    ```
    docker build -t nombre-de-la-imagen .
    ```

    Reemplaza `nombre-de-la-imagen` con un nombre descriptivo para tu imagen. El punto al final del comando indica que el `Dockerfile` se encuentra en el directorio actual.

## 3. Ejecución del Contenedor

Para ejecutar el contenedor, utiliza el siguiente comando:

deploy.ps1

Para iniciar el servicio ejecutaremos el comando:

docker-compose up


## 5. Consideraciones Adicionales

* **Rutas de Archivos:** En Windows, las rutas de archivos utilizan barras invertidas (`\`) en lugar de barras diagonales (`/`). Asegúrate de ajustar las rutas en tus comandos y scripts.

* **Permisos:** Si encuentras problemas de permisos, asegúrate de estar ejecutando la terminal como administrador y de que los archivos y directorios tengan los permisos adecuados.

* **Variables de Entorno:** Si tu aplicación utiliza variables de entorno, puedes configurarlas en PowerShell de la siguiente manera:

    ```powershell
    $env:NOMBRE_VARIABLE = "valor"
    ```


## Consideraciones de Seguridad del Diseño

Durante el diseño de la aplicación, se han tenido en cuenta las siguientes consideraciones de seguridad:

* **Autenticación:** (Explicar si tu aplicación tiene autenticación. Si no, indicar que no se implementó y por qué)
* **Autorización:** (Explicar el modelo de control de acceso. Si solo hay un usuario, indicarlo)
* **Protección de Datos:** (Cómo se protegen los datos, tanto en tránsito como en reposo.  Si usas HTTPS, indícalo)
* **Validación de Entrada:** (Cómo se valida la entrada del usuario para prevenir ataques)
* **Manejo de Errores:** (Cómo se manejan los errores para evitar revelar información sensible)
* **Dependencias:** (Qué librerías de terceros se utilizan y cómo se mantienen actualizadas)

## SDLC Seguro - Paso a Paso

A continuación, se describe el proceso de desarrollo de la aplicación To Do siguiendo un SDLC seguro:

### Fase 1: Requisitos

* Se identificaron los siguientes requisitos de seguridad:
    * (Ejemplo) Solo los usuarios autenticados pueden crear, modificar y eliminar tareas.
    * (Ejemplo) Los datos de las tareas se deben almacenar de forma segura.
    * (Ejemplo) La aplicación debe ser resistente a ataques XSS e inyección SQL.
* Estos requisitos se documentaron en este archivo `README.md` y se utilizaron para guiar el diseño y la implementación.

### Fase 2: Diseño

* Se diseñó la arquitectura de la aplicación teniendo en cuenta los requisitos de seguridad.
    * (Ejemplo) Se utilizó un framework web que proporciona protección contra XSS y CSRF.
    * (Ejemplo) Se implementó un sistema de autenticación basado en sesiones.
    * (Ejemplo) Se decidió utilizar una base de datos relacional y se utilizaron consultas parametrizadas para prevenir inyección SQL.
* El diseño de seguridad se documentó en el archivo `documentacion/diseno/diseno_seguridad.md` (o similar).

### Fase 3: Desarrollo

* Se implementaron los controles de seguridad diseñados en la fase anterior.
    * (Ejemplo) Se utilizó la librería `<nombre_de_la_librería>` para la autenticación de usuarios.  Se incluye un ejemplo de código.
    * (Ejemplo) Se validó toda la entrada del usuario utilizando la función `<nombre_de_la_función>`. Se incluye un ejemplo de código.
    * (Ejemplo) Se utilizaron consultas parametrizadas en todas las interacciones con la base de datos. Se incluye un ejemplo de código.
* Se utilizó la herramienta `SonarQube` para realizar análisis estático de código y detectar posibles vulnerabilidades.

### Fase 4: Pruebas

* Se planificaron y ejecutaron pruebas de seguridad para verificar la efectividad de los controles implementados.
    * (Ejemplo) Se realizaron pruebas de penetración básicas para identificar vulnerabilidades. Los resultados se documentaron en `documentacion/pruebas/pentest.md`.
    * (Ejemplo) Se realizaron pruebas de XSS para verificar que la aplicación no es vulnerable a este tipo de ataque. Los casos de prueba y resultados se documentaron en `documentacion/pruebas/xss.md`.
    * (Ejemplo) Se realizaron pruebas de autenticación y autorización para verificar que los usuarios solo pueden acceder a los recursos permitidos. Los casos de prueba y resultados se documentaron en `documentacion/pruebas/autenticacion.md`.

### Fase 5: Implementación

* La aplicación se implementó utilizando Docker para asegurar un entorno consistente y aislado.
    * Se proporcionó un `Dockerfile` para construir la imagen de la aplicación.
    * Se configuró el servidor para utilizar HTTPS y se obtuvo un certificado de Let's Encrypt.
    * Se utilizaron variables de entorno para gestionar las credenciales de la base de datos.

### Fase 6: Mantenimiento

* Se estableció un plan de mantenimiento de seguridad para asegurar la seguridad continua de la aplicación.
    * Se aplicarán parches de seguridad al sistema operativo y a las dependencias de la aplicación de forma regular.
    * Se monitorizarán los registros de la aplicación en busca de actividades sospechosas.
    * Se realizarán auditorías de seguridad periódicas.
    * Se actualizará la aplicación para corregir nuevas vulnerabilidades.
