from rest_framework import generics
from ..models import Cidade
from ..serializers import CidadeSerializer


class CidadeListCreateView(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class CidadeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
