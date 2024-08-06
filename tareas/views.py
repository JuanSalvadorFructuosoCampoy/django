from django.shortcuts import get_object_or_404, render, redirect

# Con esto, podemos usar un formulario de registro de usuario predeterminado por Django.
from django.contrib.auth.forms import UserCreationForm

# Importamos el formulario de autenticación de Django, para iniciar sesión de un usuario registrado
from django.contrib.auth.forms import AuthenticationForm

# Importamos el modelo de usuario de Django, para guardar los datos del usuario
from django.contrib.auth.models import User

# Importamos el sistema para guardar cookies, para logout y para autenticar un usuario que se ha introducido en el formulario de login
from django.contrib.auth import login, logout, authenticate

# Importamos el sistema para capturar errores de integridad de la base de datos
from django.db import IntegrityError

# Importamos el modelo de formulario de tareas creado en forms.py
from .forms import TareaForm

# Importamos el modelo de tareas creado en models.py
from .models import Tarea

# Create your views here.

# * Función de registro de usuario
def signup(request):
    if request.method == "GET":
        # Renderizamos el formulario preestablecido por Django, además envía una variable llamada form, que es un formulario de creación de usuario. En el template de singup.html encontraremos entre llaves una variable llamada form, que es el formulario de creación de usuario.
        return render(request, 'signup.html', {'form': UserCreationForm})
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
    # Obtenemos todas las tareas de la base de datos
    #! tareas = Tarea.objects.all()
    # El anterior mostraba todas las tareas, ahora solo mostramos las tareas del usuario que ha iniciado sesión. En el segundo filtro indicamos que la fecha de completado sea nula, para que solo muestre las tareas que no han sido completadas.
    tareas = Tarea.objects.filter(usuario=request.user, fechaCompletado__isnull=True)
    
    # Renderizamos la página de tareas, enviando las tareas obtenidas de la base de datos
    return render(request, 'tareas.html',{
        'tareas': tareas
    })

# * Función que permite cerrar la sesión del usuario
def cerrarSesion(request):
    logout(request)
    return redirect('home')

# * Función que permite iniciar sesión a un usuario ya registrado
def iniciarSesion(request):
    if request.method == "GET":
        return render(request, 'iniciarSesion.html',{
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if usuario is None:
            return render(request, 'iniciarSesion.html',{
                'form': AuthenticationForm,
                'error': 'Usuario y/o contraseña incorrectos'
            })
        else:
            login(request, usuario)
            return redirect('tareas')

def nuevaTarea(request):
    if request.method == 'GET':
        return render(request, 'nuevaTarea.html', {
            'form': TareaForm()
        })
    else:
        try:
            formulario = TareaForm(request.POST) # Creamos un formulario con los datos enviados por el usuario
            nuevaTarea = formulario.save(commit=False) # Guardamos el formulario en una variable
            nuevaTarea.usuario = request.user # Asignamos el usuario que ha creado la tarea
            nuevaTarea.save() # Guardamos la tarea en la base de datos
            return redirect('tareas') # Redirigimos a la página de tareas
        except ValueError:
            return render(request, 'nuevaTarea.html', {
                'form': TareaForm(),
                'error': 'Error al guardar la tarea'
                })

#* Muestra el detalle de una tarea
def detalleTarea(request, idTarea):
    # Obtenemos la tarea con el id que se ha pasado por parámetro, si no existe, nos muestra un 404
    tarea = get_object_or_404(Tarea, pk=idTarea)
    return render(request, 'detalleTarea.html',{
        'tarea': tarea
    })
        
