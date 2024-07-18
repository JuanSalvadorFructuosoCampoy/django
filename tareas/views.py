from django.shortcuts import render

# Con esto, podemos usar un formulario de registro de usuario predeterminado por Django.
from django.contrib.auth.forms import UserCreationForm

# Importamos el modelo de usuario de Django, para guardar los datos del usuario
from django.contrib.auth.models import User

from django.http import HttpResponse
# Create your views here.


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
                return HttpResponse("Usuario registrado correctamente")
            except:
                # Renderizamos el formulario preestablecido por Django, esta vez con un mensaje de error indicando que el usuario ya existe
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe',
                })
        else:
            # Renderizamos el formulario preestablecido por Django, indicando el error de que las contraseñas no coinciden
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden',
            })

        # !print("Enviando datos")
        # !print("Datos enviados: ", request.POST)


def home(request):
    return render(request, 'home.html')
