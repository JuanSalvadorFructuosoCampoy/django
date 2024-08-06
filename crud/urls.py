"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tareas import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    # El atributo name permite usar el nombre de la URL en lugar de la URL en sí a la hora de redireccionar, por ejemplo, en un archivo HTML.
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareasCompletadas/', views.tareasCompletadas, name='tareasCompletadas'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('signin/', views.iniciarSesion, name='signin'),
    path('tareas/crear/', views.nuevaTarea, name='tareaNueva'),
    # La URL de detalleTarea recibe un parámetro, el id de la tarea que se quiere ver
    path('tareas/<int:idTarea>/', views.detalleTarea, name='detalleTarea'),
    path('tareas/<int:idTarea>/completar/', views.completarTarea, name='completarTarea'),
    path('tareas/<int:idTarea>/eliminar/', views.eliminarTarea, name='eliminarTarea'),
]
