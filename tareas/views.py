from django.shortcuts import render
# Con esto, podemos usar un formulario de registro de usuario predeterminado por Django.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method=="GET":
        print("Mostrando formulario")
    else:
        print("Enviando datos")
        print("Datos enviados: ", request.POST)
    
  # Renderizamos el formulario preestablecido por Django
    return render(request, 'signup.html', {'form': UserCreationForm()})
    
def home(request):
    return render(request, 'home.html')
