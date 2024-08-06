from django.forms import ModelForm
from .models import Tarea

# * Se crea de forma dinámica el formulario de tareas, basado en el modelo de tareas
class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'importante']
        