from django.db import models

class Lugar(models.Model):
    nombre = models.CharField(max_length=30)    

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Estado(Lugar):
    pass


class Alcaldia(Lugar):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

