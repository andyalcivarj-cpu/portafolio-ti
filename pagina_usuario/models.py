from django.db import models


class InformacionPersonal(models.Model):
    # Campos principales obligatorios pero con blank=True para evitar problemas en migraciones
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos", blank=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres", blank=True)

    @property
    def nombre_completo(self):
        return f"{self.nombres or ''} {self.apellidos or ''}".strip() or "Sin nombre registrado"

    titulo_profesional = models.CharField(max_length=100, blank=True, verbose_name="Título Profesional")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono_convencional = models.CharField(max_length=20, blank=True, verbose_name="Teléfono Convencional")
    telefono_movil = models.CharField(max_length=20, blank=True, verbose_name="Teléfono Móvil")
    ubicacion = models.CharField(max_length=150, blank=True, verbose_name="Ubicación / Ciudad")
    nacionalidad = models.CharField(max_length=50, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True, verbose_name="Lugar de Nacimiento")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero_cedula = models.CharField(max_length=20, unique=True, blank=True, verbose_name="Número de Cédula")

    SEXO_CHOICES = [('H', 'Hombre'), ('M', 'Mujer')]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True)
    estado_civil = models.CharField(max_length=50, blank=True, verbose_name="Estado Civil")
    licencia_conducir = models.CharField(max_length=20, blank=True, verbose_name="Licencia de Conducir")
    direccion_domiciliaria = models.CharField(max_length=150, blank=True)
    direccion_trabajo = models.CharField(max_length=150, blank=True)
    sitio_web = models.URLField(blank=True, verbose_name="Sitio Web Personal")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    resumen_profesional = models.TextField(blank=True, verbose_name="Resumen / Perfil Profesional")
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    perfil_activo = models.BooleanField(default=True, verbose_name="Perfil Activo")

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Información Personal"


class Experiencia(models.Model):
    empresa = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    responsabilidades = models.TextField(blank=True, verbose_name="Funciones y Responsabilidades")
    lugar_empresa = models.CharField(max_length=100, blank=True)
    email_empresa = models.EmailField(blank=True)
    sitio_web_empresa = models.URLField(blank=True)
    nombre_contacto = models.CharField(max_length=100, blank=True, verbose_name="Referencia Laboral - Nombre")
    telefono_contacto = models.CharField(max_length=20, blank=True, verbose_name="Referencia Laboral - Teléfono")
    email_contacto = models.EmailField(blank=True, verbose_name="Referencia Laboral - Email")
    certificado_file = models.FileField(upload_to='certificados/experiencia/', blank=True, null=True)
    mostrar_en_cv = models.BooleanField(default=True, verbose_name="Mostrar en CV Público")

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name_plural = "Experiencias"


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    total_horas = models.PositiveIntegerField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    certificado_url = models.URLField(blank=True)
    certificado_file = models.FileField(upload_to='certificados/cursos/', blank=True, null=True)
    nombre_contacto = models.CharField(max_length=100, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    email_contacto = models.EmailField(blank=True)
    mostrar_en_cv = models.BooleanField(default=True, verbose_name="Mostrar en CV Público")

    class Meta:
        ordering = ['-fecha_fin', '-fecha_inicio']
        verbose_name_plural = "Cursos"


class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=[('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')], blank=True)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    entidad = models.CharField(max_length=200, blank=True, verbose_name="Entidad Patrocinadora")
    nombre_contacto = models.CharField(max_length=100, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    imagen = models.ImageField(upload_to='reconocimientos/', blank=True, null=True)
    certificado_file = models.FileField(upload_to='certificados/reconocimientos/', blank=True, null=True)
    mostrar_en_cv = models.BooleanField(default=True, verbose_name="Mostrar en CV Público")

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = "Reconocimientos"


class Garage(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del producto")
    ESTADO_CHOICES = [('Bueno', 'Bueno'), ('Regular', 'Regular')]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Bueno', verbose_name="Estado del producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor del bien ($)")
    fecha_publicacion = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Fecha de publicación")
    imagen = models.ImageField(upload_to='garage/', blank=True, null=True, verbose_name="Imagen del producto")
    mostrar_en_cv = models.BooleanField(default=True, verbose_name="Mostrar en CV Público")

    def __str__(self):
        return self.nombre or "Producto sin nombre"

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = "Producto en Garage"
        verbose_name_plural = "Productos en Garage / Ventas"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    url = models.URLField(blank=True, verbose_name="Enlace")
    tecnologias = models.CharField(max_length=300, blank=True, verbose_name="Tecnologías usadas")
    mostrar_en_cv = models.BooleanField(default=True, verbose_name="Mostrar en CV Público")

    def __str__(self):
        return self.nombre or "Proyecto sin nombre"

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = "Proyectos"