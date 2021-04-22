from django.urls import path
from usuarios import views

urlpatterns = [
    path('' , views.Usuarios),
    path('<id>/' , views.DetalleUsuario),
]
