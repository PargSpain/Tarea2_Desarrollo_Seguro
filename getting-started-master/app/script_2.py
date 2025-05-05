# Crear la estructura base del proyecto en un entorno de ejemplo.
import os

base_dirs = [
    "C:\Users\sambo\Desktop\getting-started-master/app/src"
    "C:\Users\sambo\Desktop\getting-started-master/app/spec"
    "C:\Users\sambo\Desktop\getting-started-master/docs"
    "C:\Users\sambo\Desktop\getting-started-master/tests/docker"
    "C:\Users\sambo\Desktop\getting-started-master/security"
]

files = {
    "C:\Users\sambo\Desktop\getting-started-master/security/amenazas.md": "# Amenazas\n\nAquí se describen las amenazas identificadas."
    "C:\Users\sambo\Desktop\getting-started-master/security/controles.md": "# Controles de Seguridad\n\nMedidas implementadas para mitigar riesgos."
    "C:\Users\sambo\Desktop\getting-started-master/security/checklist.md": "# Checklist de Seguridad\n\n- [ ] Validaciones\n- [ ] Autenticación\n- [ ] Control de accesos"
    "C:\Users\sambo\Desktop\getting-started-master/README.md": "# Aplicación ToDo\n\nDocumentación e instrucciones para el despliegue y seguridad."
    "C:\Users\sambo\Desktop\getting-started-master/.gitignore": "node_modules/\n__pycache__/\n.env"
    "C:\Users\sambo\Desktop\getting-started-master/tests/docker/dockerfile.test": "# Dockerfile para pruebas"
}

# Crear directorios
for dir_path in base_dirs:
    os.makedirs(dir_path, exist_ok=True)

# Crear archivos base
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

"Directorio y archivos base creados correctamente."
