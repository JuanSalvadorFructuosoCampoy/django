from django.contrib import admin
# * Importamos el modelo de tarea
from .models import tarea

#* Esto es para crear un campo de solo lectura que muestre la fecha de creación de la tarea, luego la tenemos que importar en el admin.site.register
class tareaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', )

# Register your models here.
# * Registrando el modelo de tarea en el administrador de Django para poder visualizarlo
admin.site.register(tarea,tareaAdmin)