from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    ejercicio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=240)
    gymrat = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="gymrat")
    imagen = models.ImageField(upload_to="publicacion", null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.ejercicio}"
    
class Perfil(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="perfil")
    redes_sociales = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    imagen = models.ImageField(upload_to="perfil", null=True, blank=True)

class Correo(models.Model):
    correo = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")
    imagen = models.ImageField(upload_to="correo", null=True, blank=True)