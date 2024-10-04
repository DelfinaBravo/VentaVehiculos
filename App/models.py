from django.db import models

# Create your models here.
class Vehiculos(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=30)
    Marca=models.TextField(max_length=30)
    Precio=models.IntegerField(max_length=30)
    Lugar=models.TextField(max_length=20)
    Imagen=models.ImageField(upload_to="autos",null=True)

    def __int__(self):
        self.Codigo