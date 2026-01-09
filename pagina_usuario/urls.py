from django.urls import path
from .views import hoja_de_vida

urlpatterns = [
    path('', hoja_de_vida, name='hoja_de_vida'),  # La página principal de la app
]