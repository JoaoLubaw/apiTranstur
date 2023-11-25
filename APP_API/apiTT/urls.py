from django.urls import path
from .views import CidadeRetrieveUpdateDestroyView, CidadeListCreateView
from .views import ContatoListCreateView, ContatoRetrieveUpdateDestroyView
from .views import InfoListCreateView, InfoRetrieveUpdateDestroyView
from .views import PontoFisicoRetrieveUpdateDestroyView, PontoFisicoListCreateView
from .views import SlideListCreateView, SlideRetrieveUpdateDestroyView

urlpatterns = [
    path('app/cidades/', CidadeListCreateView.as_view(), name='cidade-list-create'),
    path('app/cidades/<int:pk>/', CidadeRetrieveUpdateDestroyView.as_view(), name='cidade-retrieve-update-destroy'),

    path('app/contatos/', ContatoListCreateView.as_view(), name='contato-list-create'),
    path('app/contatos/<int:pk>/', ContatoRetrieveUpdateDestroyView.as_view(), name='contato-retrieve-update-destroy'),

    path('app/infos/', InfoListCreateView.as_view(), name='info-list-create'),
    path('app/infos/<int:pk>/', InfoRetrieveUpdateDestroyView.as_view(), name='info-retrieve-update-destroy'),

    path('app/pontosfisicos/', PontoFisicoListCreateView.as_view(), name='pontofisico-list-create'),
    path('app/pontosfisicos/<int:pk>/', PontoFisicoRetrieveUpdateDestroyView.as_view(), name='pontofisico-retrieve-'
                                                                                             'update-destroy'),
    path('app/slides/', SlideListCreateView.as_view(), name='slide-list-create'),
    path('app/slides/<int:pk>/', SlideRetrieveUpdateDestroyView.as_view(), name='slide-retrieve-update-destroy'),

]
