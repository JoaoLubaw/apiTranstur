from rest_framework import serializers
from .models import Cidade
from .models import Ponto
from .models import Contato
from .models import Info
from .models import PontoFisico
from .models import Slide


class PontoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ponto
    fields = ['PontoID', 'Name', 'Maps', 'Endereco']

class CidadeSerializer(serializers.ModelSerializer):
    pontos = PontoSerializer(many=True, read_only=True)
    class Meta:
        model = Cidade
        fields = ['CityId', 'Name', 'pontos']


class ContatoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Info
    fields = '__all__'


class PontoFisicoSerializer(serializers.ModelSerializer):
  class Meta:
    model = PontoFisico
    fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slide
    fields = '__all__'
