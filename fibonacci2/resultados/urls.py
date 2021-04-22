from django.urls import path
from resultados import views

urlpatterns = [
    path('' , views.Resultados),
    path('<id>/' , views.DetalleResultado),
]
