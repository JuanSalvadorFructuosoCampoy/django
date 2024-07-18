from django.shortcuts import render, redirect

# Con esto, podemos usar un formulario de registro de usuario predeterminado por Django.
from django.contrib.auth.forms import UserCreationForm

# Importamos el modelo de usuario de Django, para guardar los datos del usuario
from django.contrib.auth.models import User

# Importamos el sistema para guardar cookies
from django.contrib.auth import login

# Importamos el sistema para capturar errores de integridad de la base de datos
from django.db import IntegrityError

# Create your views here.

# * Función de registro de usuario
def signup(request):
    if request.method == "GET":
        # Renderizamos el formulario preestablecido por Django
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Esto es un bloque try-except, que se utiliza para capturar errores
            try:
                # Registro de usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # * Guardamos la cookie de sesión, para mantener los datos del usuario guardados en una cookie
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                # Renderizamos el formulario preestablecido por Django, esta vez con un mensaje de error indicando que el usuario ya existe
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe',
                })
        else:
            # Renderizamos el formulario preestablecido por Django, indicando el error de que las contraseñas no coinciden
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden',
            })

        # !print("Enviando datos")
        # !print("Datos enviados: ", request.POST)

# * Función de la página home
def home(request):
    return render(request, 'home.html')

# * Función de la página que permite visualizar las tareas
def tareas(request):
    return render(request, 'tareas.html')
