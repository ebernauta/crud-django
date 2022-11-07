from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='rut')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    email = models.CharField(max_length=50 , verbose_name='email')
    contrasena = models.CharField(max_length=50, verbose_name='contrasena')
    ingreso = models.CharField(max_length=50, verbose_name='ingreso')

    def __str__(self):
        return self.nombre