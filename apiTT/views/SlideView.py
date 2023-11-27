from rest_framework import generics
from ..models import Slide
from ..serializers import SlideSerializer


class SlideListCreateView(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class SlideRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
