## Consideraciones de seguridad hecha durante el diseño de la aplicación

### Fase de Requisitos

* **Datos:** La aplicación maneja una lista de tareas. Se prioriza la integridad de estos datos.
* **Usuarios y Roles:**
    * Versión básica: Un solo rol de administrador.
    * Versión avanzada: Roles de administrador, usuario normal e invitado.
* **Autenticación:**
    * Versión básica: No se requiere autenticación.
    * Versión avanzada: Autenticación basada en nombre de usuario y contraseña (o tokens).
* **Protección de Datos:**
    * En tránsito: Se usará HTTPS para la comunicación web.
    * En reposo: Se protegerá la integridad de la base de datos.
* **Vulnerabilidades Potenciales:**
    * Inyección SQL (si se usa una base de datos SQL).
    * XSS (si se muestra la lista de tareas en una página web).
    * CSRF (si hay acciones que modifican datos).

### Fase de Desarrollo

* **Herramientas utilizadas:**
    * Hemos optado por scripts de desarrollo propio para esta tarea.
    * Se encuentran alojados en las carpetas secutity/
    * Se pueden incluir herramientas de análisis estático e integrarlas en el proyecto. Por falta de tiempo y conocimientos no se ha realizado.

### Fase de pruebas

* **Planificación:**
    * En la carpeta tests/pruebas encontraremos los script propuestos.
    * Se pueden desarrollar más e incluir en el proyecto.

## Despliegue

La aplicación To-Do se puede desplegar utilizando Docker. Se proporciona un `Dockerfile` para construir la imagen de la aplicación.

### Requisitos

# ## Para Linux:

* Docker instalado.

### Pasos

1.  Clonar este repositorio:
    `git clone <URL del repositorio>`
2.  Navegar al directorio del proyecto:
    `cd proyecto_sdlc_seguro`
3.  Construir la imagen de Docker:
    `docker build -t todo-app .`
4.  Ejecutar la imagen de Docker:
    `docker run -p 8000:8000 todo-app` (La aplicación se ejecuta en el puerto 8000 por decisión propia, pero se puede ejecutar en otro puerto)


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


### Despliegue Seguro

* La aplicación se despliega en un contenedor Docker, lo que proporciona aislamiento y reduce el riesgo de que otras aplicaciones en el mismo sistema afecten a la aplicación To-Do.
* Se recomienda utilizar un servidor web proxy (ej., Nginx) en frente del contenedor de la aplicación para manejar las solicitudes HTTPS y proporcionar una capa adicional de seguridad.
* El servidor web proxy debe configurarse para usar un certificado SSL/TLS válido.
* El acceso al servidor debe estar protegido por un firewall que solo permita el tráfico necesario.
* Las variables de entorno se utilizan para configurar la aplicación, incluyendo cualquier secreto o credencial. Estas variables se pasan al contenedor en tiempo de ejecución y no se incluyen en la imagen de Docker.


## Mantenimiento de Seguridad

El mantenimiento de la seguridad de la aplicación To-Do es un proceso continuo que podría incluir las siguientes actividades:

* **Actualizaciones de Seguridad:**
    * El sistema operativo del servidor se actualizará mensualmente con los últimos parches de seguridad.
    * El servidor web (ej., Nginx) se actualizará trimestralmente.
    * La aplicación To-Do y sus dependencias se actualizarán trimestralmente para corregir vulnerabilidades y obtener nuevas características de seguridad.
* **Monitorización de Seguridad:**
    * Se implementará un sistema de registro centralizado para recopilar y analizar los registros de la aplicación y del servidor.
    * Se configurarán alertas para detectar actividades sospechosas, como intentos de inicio de sesión fallidos, errores inusuales o tráfico de red sospechoso.
    * Se utilizará una herramienta de monitorización de seguridad (ej., OSSEC, Fail2ban) para detectar y bloquear ataques comunes.
* **Auditorías de Seguridad:**
    * Se realizarán pruebas de penetración anuales para identificar posibles vulnerabilidades en la aplicación y la infraestructura.
    * Se utilizará una herramienta de análisis de vulnerabilidades (ej., OpenVAS, Nessus) para escanear la aplicación en busca de vulnerabilidades conocidas.
* **Respuesta a Incidentes:**
    * Se ha desarrollado un plan de respuesta a incidentes para manejar cualquier incidente de seguridad que pueda ocurrir. Este plan incluye los pasos a seguir para contener el incidente, erradicar la causa raíz y recuperar la aplicación.
    * El equipo de desarrollo y operaciones de seguridad revisará y actualizará el plan de respuesta a incidentes anualmente.


* ** En una fase posterior (Tarea 2) se ha añadió el script fuzzing.py para automatizar el envío de datos maliciosos a la API de la aplicación To Do. Esto permite detectar vulnerabilidades de inyección o errores no controlados de manera automatizada.

* ** También se ha añadido el script run_zap.py que conjuntamente con la herramienta ZAP instalado en nuestro equipo nos permitirá para ampliar las pruebas de seguridad.