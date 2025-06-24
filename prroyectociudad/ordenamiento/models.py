from django.db import models

# Create your models here.
class Parroquia(models.Model):
    opciones_ubi = (
        ('norte', 'norte'),
        ('sur', 'sur'),
        ('este', 'este'),
        ('oeste', 'oeste')
    )

    opciones_tipo = (
        ('urbana', 'urbana'),
        ('rural', 'rural')
    )

    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(
        max_length=10,
        choices=opciones_ubi)
    tipo = models.CharField(
        max_length=10,
        choices=opciones_tipo)
    
    def __str__(self):
        return f"{self.nombre} ({self.ubicacion}) - {self.tipo}"
    

class Barrio(models.Model):
    opciones_parque = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    nombre = models.CharField(max_length=200)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=opciones_parque)
    numero_edificios_residenciales = models.IntegerField()

    parroquia = models.ForeignKey(
        Parroquia,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nombre} \
            Viviendas: {self.numero_viviendas} \
            Parques: {self.numero_parques} \
            Edificios residenciales: {self.numero_edificios_residenciales} \
            Parroquia: {self.parroquia.nombre}"
