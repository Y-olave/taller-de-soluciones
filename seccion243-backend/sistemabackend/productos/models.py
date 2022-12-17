from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos')
    
class usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='usuarios')
