from django.db import models
from django.utils import timezone
# Create your models here.

class Misperris(models.Model):
    nombre=models.CharField(max_length=50)
    Raza_Predominante=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.Raza_Predominante, self.descripcion, self.estado)

class Socio(models.Model):
    TIPO_VIVIENDA = [
        (1, 'Casa con patio Grande'),
        (2, 'Casa con Patio Pequeño'),
        (3, 'Casa sin patio'),
        (4, 'Departamento'),
    ]

    correo= models.EmailField()
    rut = models.CharField(max_length=15, verbose_name= 'RUT')
    nombre= models.CharField(max_length=100, verbose_name="Nombre Completo")
    fecha_nacimiento= models.DateField()
    telefono= models.CharField(max_length= 9, verbose_name='Telefono')
    ciudad= models.CharField(max_length=50, verbose_name='Ciudad')
    vivienda= models.IntegerField(choices=TIPO_VIVIENDA)

    def __str__(self):
        return self.nombre