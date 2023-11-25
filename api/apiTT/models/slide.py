from django.db import models


def nome_img(instance, filename):
    extensao = filename.split('.')[-1]  # Obtém a extensão do arquivo
    # Verifica se instance.IMG_ID é None e usa uma string vazia nesse caso
    img_id = instance.IMG_ID or ""
    nome_arq = f"Imagem{img_id}.{extensao}"  # Define o nome do arquivo como "ImagemID + extensão"
    return f"medias/slides/{nome_arq}"  # Substitua "caminho/do/destino/" pelo caminho desejado


class Slide(models.Model):
    IMG_ID = models.AutoField(primary_key=True)
    Imagem = models.ImageField(upload_to=nome_img)
    Conteudo = models.CharField(max_length=200, default='', null=True, blank=True)

    @property
    def imagem_adress(self):
        return nome_img(self, self.Imagem.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.Conteudo:
            self.Conteudo = f'Imagem{self.IMG_ID}'


    def __str__(self):
        return str(self.IMG_ID)
