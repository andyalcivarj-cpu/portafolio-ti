from django.urls import path
from . import views

# ESTA LÍNEA ES LA QUE FALTA Y CAUSA EL ERROR
app_name = 'pagina_usuario'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('hoja-de-vida/', views.hoja_de_vida, name='hoja_de_vida'),
    path('cv/imprimir/', views.cv_imprimir, name='cv_imprimir'),
    path('cv/descargar-pdf/', views.cv_pdf, name='cv_pdf'),
]