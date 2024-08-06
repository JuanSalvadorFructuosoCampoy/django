Crear entorno virtual para proyecto: py -m venv venv

Una vez creado, para activarlo: IMPORTANTE: hay que estar dentro de la carpeta venv creada con el comando anterior Scripts\activate

Instalar django: python -m pip install Django

Iniciar nuevo projecto: django-admin startproject . El punto final permite que se cree directamente dentro de la carpeta en la que nos encontramos

Arrancar el proyecto: Hay que estar en la carpeta donde se encuentre el archivo manage.py python manage.py runserver

Para personalizar el puerto en el que sale: python manage.py runserver

Crear una nueva aplicación dentro del proyecto: Python manage.py startapp

Activar virtualenv: Scripts\actívate

Crear super usuario para entrar en la administración de Python: python manage.py createsuperuser

Django crea su propia base de datos, que podemos explorar con el programa DB Browser for SQLite. Para crear tablas, entramos en el archivo models.py, creamos el modelo y luego ejecutamos los comandos python manage.py makemigrations y luego python manage.py migrate. Con esto, migramos los modelos a la base de datos.
