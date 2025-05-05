## Diseño de Seguridad: Aplicación To-Do

### 1.  Arquitectura General

La aplicación sigue una arquitectura de tres capas:

* **Capa de Presentación:** Interfaz de usuario (web o de línea de comandos).
* **Capa de Lógica de Negocio:** Maneja la creación, modificación y eliminación de tareas.
* **Capa de Datos:** Almacena las tareas (en memoria, en un archivo o en una base de datos).


### 2.  Autenticación y Autorización (Versión Avanzada)

* **Autenticación:** Se puede utilizar JWT (JSON Web Tokens) para la autenticación. El servidor generará un token después de que el usuario proporcione credenciales válidas. Este token se enviará en las peticiones posteriores.
* **Autorización:** Se implementará un sistema de control de acceso basado en roles (RBAC). Los roles serán:
    * Administrador: Puede crear, leer, actualizar y eliminar cualquier tarea.
    * Usuario normal: Puede crear, leer, actualizar y eliminar solo sus propias tareas.
    * Invitado: Solo puede leer todas las tareas.


### 3.  Manejo de Datos

* **En tránsito:** Se utilizará HTTPS para cifrar todas las comunicaciones entre el cliente y el servidor. Se obtendrá un certificado TLS de una CA confiable.
* **En reposo:**
    * Opción 1 (Archivo): Si las tareas se guardan en un archivo, se calculará un hash criptográfico del archivo periódicamente para detectar modificaciones no autorizadas.
    * Opción 2 (Base de datos): Si se usa una base de datos, se utilizarán transacciones para asegurar la integridad de los datos. Se implementarán copias de seguridad periódicas.

### 4.  Medidas de Seguridad Adicionales

* **Validación de Entrada:** Todas las entradas del usuario se validarán en el servidor para prevenir inyección de código y otros ataques.
* **Sanitización de Salida:** Los datos mostrados en la interfaz de usuario se sanitizarán para prevenir XSS.
* **Protección contra CSRF:** Se implementará un token CSRF en los formularios para prevenir ataques CSRF.
* **Manejo de Errores:** Los errores se manejarán de forma segura, sin mostrar información sensible al usuario.