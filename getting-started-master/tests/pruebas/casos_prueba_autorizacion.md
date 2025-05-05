# Pruebas de Autorización

## Descripción:
Verificar que los usuarios solo puedan acceder a los recursos y realizar las acciones permitidas por sus roles.

## Pasos:

1.  Crear un usuario con rol de "usuario normal".

2.  Crear un usuario con rol de "administrador".

3.  Iniciar sesión con el usuario normal e intentar eliminar una tarea creada por otro usuario.

4.  Verificar que la aplicación no permita eliminar la tarea.

5.  Iniciar sesión con el usuario administrador e intentar eliminar la tarea creada por el usuario normal.

6.  Verificar que la aplicación permita eliminar la tarea.

## Resultado Esperado:
Los usuarios deben estar limitados a las acciones permitidas por sus roles.


## Resultado:

Autorización exitosa para usuario_normal en http://localhost:8000/admin
Autorización exitosa para administrador en http://localhost:8000/admin