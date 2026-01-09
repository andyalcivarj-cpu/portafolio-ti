from django.shortcuts import render
from .models import (
    InformacionPersonal,
    Educacion,
    Experiencia,
    Habilidad,
    Idioma,
    Proyecto,
    Certificacion
)

def hoja_de_vida(request):
    # Información principal (asumimos solo hay un registro)
    info_personal = InformacionPersonal.objects.first()
    
    context = {
        'info_personal': info_personal,
        'educaciones': Educacion.objects.all().order_by('-fecha_inicio'),
        'experiencias': Experiencia.objects.all().order_by('-fecha_inicio'),
        'habilidades': Habilidad.objects.all(),
        'idiomas': Idioma.objects.all(),
        'proyectos': Proyecto.objects.all().order_by('-fecha'),                  # Nuevo
        'certificaciones': Certificacion.objects.all().order_by('-fecha_obtencion'),  # Nuevo
    }
    
    return render(request, 'pagina_usuario/hoja_de_vida.html', context)
