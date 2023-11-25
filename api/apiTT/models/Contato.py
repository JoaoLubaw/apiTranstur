from django.db import models

class Contato(models.Model):

    OPCOES_CONTATO = (
      ('whatsapp', 'Whatsapp'),
      ('telefone', 'Telefone'),
      ('email', 'Email'),
    )

    ContatoID = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=OPCOES_CONTATO)
    Conteudo = models.CharField(max_length=100)

    def __str__(self):
        return self.Conteudo
