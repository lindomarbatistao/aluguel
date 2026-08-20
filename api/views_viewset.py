from rest_framework.viewsets import ModelViewSet
from .models import (Usuario, Imovel, Contrato, Pagamento)
from .serializers import (UsuarioSerializer, ImovelSerializer,
    ContratoSerializer, PagamentoSerializer)
from .filters import UsuarioFilter, ImovelFilter
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter
    

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImovelFilter

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer