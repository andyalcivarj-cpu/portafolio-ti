import os
import django

# Asegúrate de que 'proyecto.settings' coincida con el nombre de tu carpeta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='Andy').exists():
    User.objects.create_superuser('Andy', 'andyalcivar@gmail.com', 'domingo9')
    print("Súperusuario creado exitosamente")
else:
    print("El súperusuario ya existe")