from django.db import models
# * Importamos el modelo de usuario de Django, para guardar los datos del usuario
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fechaCompletado = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # * Esto es para que se vea el título del proyecto y el autor en el administrador de Django
    def __str__(self):
        return self.titulo + ' de ' + self.usuario.username