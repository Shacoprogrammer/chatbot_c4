from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class DatosUsuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=250)
    fecha_hora = models.DateTimeField()
    creador = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)
    inscripcion_fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evento.nombre} - {self.usuario.username}"
