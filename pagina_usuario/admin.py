from django.contrib import admin
from .models import (
    InformacionPersonal,
    Experiencia,
    Curso,
    Reconocimiento,
    Proyecto,
    Garage,
    # ProductoLaboral está comentado porque parece que no existe en models.py actual
    # Si después lo agregas, descoméntalo
)

@admin.register(InformacionPersonal)
class InformacionPersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'email', 'telefono_movil', 'nacionalidad', 'perfil_activo']
    search_fields = ['nombres', 'apellidos', 'email', 'numero_cedula']
    list_filter = ['perfil_activo', 'sexo']


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'mostrar_en_cv']
    list_filter = ['mostrar_en_cv']
    search_fields = ['cargo', 'empresa']
    date_hierarchy = 'fecha_inicio'


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'institucion', 'fecha_fin', 'mostrar_en_cv']
    list_filter = ['mostrar_en_cv']
    search_fields = ['nombre', 'institucion']
    date_hierarchy = 'fecha_fin'


@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'fecha', 'mostrar_en_cv']
    list_filter = ['mostrar_en_cv', 'tipo']
    search_fields = ['titulo', 'entidad']


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mostrar_en_cv']
    list_filter = ['mostrar_en_cv']
    list_editable = ['mostrar_en_cv']
    # si quieres búsqueda más adelante, cuando agregues campos:
    # search_fields = ['nombre', 'descripcion']


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'valor', 'mostrar_en_cv']
    list_filter = ['mostrar_en_cv', 'estado']
    search_fields = ['nombre']