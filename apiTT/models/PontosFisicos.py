from django.db import models

def nome_imagem(instance, filename):
    extensao = filename.split('.')[-1]  # Obtém a extensão do arquivo
    nome_arq = f"{instance.PF_ID}.{extensao}"  # Define o nome do arquivo como ID + extensão

    return f"medias/pontosfisicos/{nome_arq}"  # Substitua "caminho/do/destino/" pelo caminho desejado


class PontoFisico(models.Model):
    PF_ID = models.AutoField(primary_key=True)
    Imagem = models.ImageField(upload_to=nome_imagem)
    Endereco = models.CharField(max_length=400)
    Maps = models.CharField(max_length=500, null=True)

    @property
    def ImagemAdress(self):
        return nome_imagem(self, self.Imagem.name)

    def __str__(self):
        return self.Endereco
