# TuPrimeraPagina-Gallardo

Este es un proyecto web creado en Django para practicar el patrón MVT. Incluye modelos para publicaciones, categorías y comentarios, formularios para insertar datos, y una funcionalidad de búsqueda.

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual y activarlo.
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

   python -m django startproject blog_project

   python manage.py startapp blog

   python manage.py makemigrations

   python manage.py migrate

   python manage.py runserver 
