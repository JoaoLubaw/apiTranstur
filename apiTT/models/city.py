from django.db import models

class Cidade(models.Model):
    objects = None
    CityId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.Name

class Ponto(models.Model):
    PontoID = models.AutoField(primary_key=True)
    City = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name="pontos")
    Name = models.CharField(max_length=200)
    Maps = models.CharField(max_length=500, null=True, blank=True)
    Endereco = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Name
