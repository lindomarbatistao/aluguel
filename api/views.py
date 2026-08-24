from rest_framework.viewsets import ModelViewSet
from .models import (Usuario, Imovel, Contrato, Pagamento)
from .serializers import (UsuarioSerializer, ImovelSerializer,
    ContratoSerializer, PagamentoSerializer)

from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter
    
    
    @action(
        detail = False,
        methods = ["get"],
        permission_classes = [IsAdminUser]
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
    
    @action(
            detail = False,
            methods = ["get"],
            permission_classes = [IsAdminUser]
        )
    def titulos(self, request):
        imoveis = Imovel.objects.all()
        dados = [
            imovel.titulo
            for imovel in imoveis
        ]
        return Response(dados)

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratoFilter
    
    @action(
            detail = False,
            methods = ["get"],
            permission_classes = [IsAdminUser]
        )
    def usuarios(self, request):
        contratos = Contrato.objects.all()
        dados = [
            {
                "numero": contrato.id,
                "locador": contrato.locador.get_full_name(),
                "locatario": contrato.locatario.get_full_name()
            }
            for contrato in contratos
        ]
        return Response(dados)

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = PagamentoFilter
    
    @action(
                detail = False,
                methods = ["get"],
                permission_classes = [IsAdminUser]
            )
    def locatarios(self, request):
        pagamentos = Pagamento.objects.all()
        
        dados = [
            {
                "locatario": pagamento.contrato.locatario.get_full_name(),
                "valor": pagamento.valor,
                "data_pagamento": pagamento.data_pagamento
            }
            for pagamento in pagamentos
        ]
        return Response(dados)