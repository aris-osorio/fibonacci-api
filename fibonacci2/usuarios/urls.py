from django.urls import path
from usuarios import views

urlpatterns = [
    path('' , views.Usuarios),
    path('login/',views.Login),
    path('<id>/' , views.DetalleUsuario),
]
