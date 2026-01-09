from django.db import models

# Modelo principal: Información personal (solo debería haber UNA entrada por usuario)
class InformacionPersonal(models.Model):
    nombre_completo = models.CharField(max_length=100)
    titulo_profesional = models.CharField(max_length=100, blank=True)  # Ej: "Desarrollador Full Stack"
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=100, blank=True)  # Ej: "Manta, Ecuador"
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    resumen_profesional = models.TextField(blank=True)  # El "Sobre mí" o resumen

    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Información Personal"


# Educación
class Educacion(models.Model):
    institucion = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)  # Puede estar en curso
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name_plural = "Educaciones"


# Experiencia laboral
class Experiencia(models.Model):
    empresa = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    responsabilidades = models.TextField(blank=True)  # Puedes listarlas con viñetas en el template

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name_plural = "Experiencias"


# Habilidades (puedes tener muchas)
class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto'),
    ]

    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='Intermedio')
    porcentaje = models.PositiveSmallIntegerField(default=50, help_text="0-100%")  # Para barras de progreso

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"

    class Meta:
        verbose_name_plural = "Habilidades"


# Idiomas (opcional pero muy útil en CV)
class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
        ('Nativo', 'Nativo'),
    ])

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200, help_text="Ej: Python, Django, PostgreSQL")
    enlace = models.URLField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Nuevo modelo: Certificacion
class Certificacion(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    fecha_obtencion = models.DateField()
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre