import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import InformacionPersonal, Experiencia, Curso, Reconocimiento, Proyecto, Garage

# --- CONFIGURACIÓN PARA WINDOWS ---
gtk_bin_path = r'C:\Program Files\GTK3-Runtime-Win64\bin'
if os.path.exists(gtk_bin_path):
    os.environ['PATH'] = gtk_bin_path + os.pathsep + os.environ.get('PATH', '')

try:
    from weasyprint import HTML
except (ImportError, OSError):
    HTML = None

def landing(request):
    return render(request, 'landing.html')

def hoja_de_vida(request):
    """Función para la visualización en el navegador"""
    info_personal = InformacionPersonal.objects.first()
    context = {
        'info_personal': info_personal,
        'experiencias': Experiencia.objects.all(),
        'cursos': Curso.objects.all(),
        'reconocimientos': Reconocimiento.objects.all(),
        'proyectos': Proyecto.objects.all(),
        'garage': Garage.objects.all(),
    }
    return render(request, 'hoja_de_vida.html', context)

def cv_imprimir(request):
    """Vista previa del formato antes de convertir a PDF"""
    info_personal = InformacionPersonal.objects.first()
    context = {
        'info_personal': info_personal,
        'mostrar_perfil': True,
        'experiencias': Experiencia.objects.all(),
        'cursos': Curso.objects.all(),
        'reconocimientos': Reconocimiento.objects.all(),
        'proyectos': Proyecto.objects.all(),
        'garage': Garage.objects.all(),
        'incluir_anexos': True,
        'mostrar_lista_cursos': True,
    }
    return render(request, 'cv_pdf_formato.html', context)

def cv_pdf(request):
    """Generación del PDF con filtros del modal"""
    if not HTML:
        return HttpResponse("Error: GTK3 no detectado.", status=500)

    # Filtros obtenidos del modal (checkboxes)
    m_perfil = request.GET.get('perfil') == 'on'
    m_exp = request.GET.get('experiencia') == 'on'
    m_cursos = request.GET.get('cursos') == 'on'
    m_logros = request.GET.get('reconocimientos') == 'on'
    m_proy = request.GET.get('proyectos') == 'on'
    m_anexos = request.GET.get('anexos') == 'on'

    info_personal = InformacionPersonal.objects.first()
    
    # Lógica de carga de datos para el PDF
    cursos_query = Curso.objects.all() if (m_cursos or m_anexos) else None

    context = {
        'info_personal': info_personal,
        'mostrar_perfil': m_perfil,
        'experiencias': Experiencia.objects.all() if m_exp else None,
        'cursos': cursos_query,
        'mostrar_lista_cursos': m_cursos,
        'reconocimientos': Reconocimiento.objects.all() if m_logros else None,
        'proyectos': Proyecto.objects.all() if m_proy else None,
        # CORRECCIÓN: Garage ahora se carga siempre para la web o puedes añadirle su propio filtro
        'garage': Garage.objects.all(), 
        'incluir_anexos': m_anexos,
    }

    html_string = render_to_string('cv_pdf_formato.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="CV_Andy_Alcivar.pdf"'

    # Generación del PDF
    HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf(response)
    return response