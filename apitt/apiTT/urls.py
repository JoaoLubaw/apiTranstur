from django.urls import path
from .views import CidadeRetrieveUpdateDestroyView, CidadeListCreateView
from .views import ContatoListCreateView, ContatoRetrieveUpdateDestroyView
from .views import InfoListCreateView, InfoRetrieveUpdateDestroyView
from .views import PontoFisicoRetrieveUpdateDestroyView, PontoFisicoListCreateView
from .views import SlideListCreateView, SlideRetrieveUpdateDestroyView

urlpatterns = [
    path('api/cidades/', CidadeListCreateView.as_view(), name='cidade-list-create'),
    path('api/cidades/<int:pk>/', CidadeRetrieveUpdateDestroyView.as_view(), name='cidade-retrieve-update-destroy'),

    path('api/contatos/', ContatoListCreateView.as_view(), name='contato-list-create'),
    path('api/contatos/<int:pk>/', ContatoRetrieveUpdateDestroyView.as_view(), name='contato-retrieve-update-destroy'),

    path('api/infos/', InfoListCreateView.as_view(), name='info-list-create'),
    path('api/infos/<int:pk>/', InfoRetrieveUpdateDestroyView.as_view(), name='info-retrieve-update-destroy'),

    path('api/pontosfisicos/', PontoFisicoListCreateView.as_view(), name='pontofisico-list-create'),
    path('api/pontosfisicos/<int:pk>/', PontoFisicoRetrieveUpdateDestroyView.as_view(), name='pontofisico-retrieve-'
                                                                                             'update-destroy'),
    path('api/slides/', SlideListCreateView.as_view(), name='slide-list-create'),
    path('api/slides/<int:pk>/', SlideRetrieveUpdateDestroyView.as_view(), name='slide-retrieve-update-destroy'),

]
