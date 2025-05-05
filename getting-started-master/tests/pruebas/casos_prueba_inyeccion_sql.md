# Pruebas de Inyección SQL

## Descripción:
Verificar que la aplicación To-Do no sea vulnerable a inyección SQL al crear, modificar o eliminar tareas.

## Pasos:

1.  Crear una tarea con un título que contenga código SQL malicioso (ej., `; DROP TABLE tareas; --`).

2.  Verificar que la base de datos no se modifique de forma inesperada.

3.  Modificar una tarea existente con un título que contenga código SQL malicioso.

4.  Verificar que la base de datos no se modifique de forma inesperada.

5.  Eliminar una tarea utilizando un ID que contenga código SQL malicioso.

6.  Verificar que solo se elimine la tarea especificada y no otras.

## Resultado Esperado:
La base de datos no debe ser modificada por el código SQL malicioso. La aplicación debe manejar la entrada de forma segura.


## Resultado:

No se detectó inyección SQL en http://localhost:8000/login con payload: ' OR '1'='1