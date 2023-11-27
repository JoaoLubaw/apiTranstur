from rest_framework import generics
from ..models import Info
from ..serializers import InfoSerializer


class InfoListCreateView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
