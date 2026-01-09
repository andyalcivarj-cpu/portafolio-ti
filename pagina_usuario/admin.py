from django.contrib import admin
from .models import (
    InformacionPersonal,
    Educacion,
    Experiencia,
    Habilidad,
    Idioma,
    Proyecto,
    Certificacion,
)

# Registro simple y limpio
admin.site.register(InformacionPersonal)
admin.site.register(Educacion)
admin.site.register(Experiencia)
admin.site.register(Habilidad)
admin.site.register(Idioma)
admin.site.register(Proyecto)
admin.site.register(Certificacion)