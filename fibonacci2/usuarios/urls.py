from django.urls import path
from usuarios import views

urlpatterns = [
    path('' , views.Usuarios),
    path('login/',views.Login),
    path('logout/',views.Logout),
    path('<id>/' , views.DetalleUsuario),
]
