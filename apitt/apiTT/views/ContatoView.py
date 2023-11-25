from rest_framework import generics
from ..models import Contato
from ..serializers import ContatoSerializer


class ContatoListCreateView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
