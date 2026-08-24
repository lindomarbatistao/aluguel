from rest_framework.viewsets import ModelViewSet
from .models import (Usuario, Imovel, Contrato, Pagamento)
from .serializers import (UsuarioSerializer, ImovelSerializer,
    ContratoSerializer, PagamentoSerializer)

from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter
    
    @action(
        detail = False,
        methods = ["get"]
    )
    def nomes(self, request):
        usuarios = Usuario.objects.all()
        nomes = [
            usuario.get_full_name()
            for usuario in usuarios
        ]
        return Response(nomes)

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImovelFilter

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratoFilter

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = PagamentoFilter