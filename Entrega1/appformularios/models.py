from django.db import models

# Create your models here.

#Aqui creo las clases para la base de datos
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=25)
    email = models.EmailField()
    sector = models.CharField(max_length=50)

class Producto(models.Model):
    id_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)


class Sucursal(models.Model):
    nombre_direccion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()