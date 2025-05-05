# Pruebas de Cross-Site Scripting (XSS)

## Descripción:
Verificar que la aplicación To-Do no sea vulnerable a XSS al mostrar los títulos de las tareas.

## Pasos:

1.  Crear una tarea con un título que contenga código HTML malicioso (ej., `<script>alert("XSS")</script>`).

2.  Verificar que el código HTML se muestre como texto plano y no se ejecute.

3.  Crear una tarea con un título que contenga un enlace malicioso (ej., `<a href="javascript:alert('XSS')">Click me</a>`).

4.  Verificar que el enlace no ejecute código JavaScript al hacer clic.

## Resultado Esperado:
El código HTML y los enlaces maliciosos se deben mostrar como texto plano, sin ejecutar código.


## Resultado:

DevTools listening on ws://127.0.0.1:51454/devtools/browser/dab6ef9b-15af-4327-b6da-a98bfd8f720e
Probando XSS en la URL: http://localhost:8000/tutorial/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/
Probando XSS en la URL: http://localhost:8000/tutorial/our-application/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/our-application/
Probando XSS en la URL: http://localhost:8000/tutorial/updating-our-app/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/updating-our-app/
Probando XSS en la URL: http://localhost:8000/tutorial/sharing-our-app/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/sharing-our-app/
Probando XSS en la URL: http://localhost:8000/tutorial/persisting-our-data/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/persisting-our-data/
Probando XSS en la URL: http://localhost:8000/tutorial/using-bind-mounts/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/using-bind-mounts/
Probando XSS en la URL: http://localhost:8000/tutorial/multi-container-apps/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/multi-container-apps/
Probando XSS en la URL: http://localhost:8000/tutorial/using-docker-compose/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/using-docker-compose/
Probando XSS en la URL: http://localhost:8000/tutorial/image-building-best-practices/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/image-building-best-practices/
Probando XSS en la URL: http://localhost:8000/tutorial/what-next/
  No se encontró el campo: title en esta página
  No se encontró el campo: description en esta página
  No se detectó XSS en la página: http://localhost:8000/tutorial/what-next/