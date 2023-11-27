from rest_framework import generics
from ..models import PontoFisico
from ..serializers import PontoFisicoSerializer


class PontoFisicoListCreateView(generics.ListCreateAPIView):
    queryset = PontoFisico.objects.all()
    serializer_class = PontoFisicoSerializer


class PontoFisicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PontoFisico.objects.all()
    serializer_class = PontoFisicoSerializer
