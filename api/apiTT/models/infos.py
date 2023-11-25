from django.db import models

class Info(models.Model):
    InfoId = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200, unique=True)
    Texto = models.TextField(default=None)

    def __str__(self):
      return self.Titulo
