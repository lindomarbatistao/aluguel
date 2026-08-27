from rest_framework.viewsets import ModelViewSet
from .models import (Usuario, Imovel, Contrato, Pagamento)
from .serializers import (UsuarioSerializer, ImovelSerializer,
    ContratoSerializer, PagamentoSerializer)

from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.db.models import Count
from io import BytesIO

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
    
    @action(detail = False, methods = ["get"],permission_classes = [IsAdminUser])
    def titulos(self, request):
        imoveis = Imovel.objects.all()
        dados = [
            imovel.titulo
            for imovel in imoveis
        ]
        return Response(dados)
    
    @action(detail=False, methods=['GET'])
    def grafico(self, request):
        dados = Imovel.objects.values("tipo").annotate(total=Count("id"))
        
        tipos = [item["tipo"] for item in dados]
        totais = [item["total"] for item in dados]
        
        plt.bar(tipos, totais)
        plt.title("Imobiliaria LogiTude")
        plt.xlabel("Tipos")
        plt.ylabel("Qde")
        
        imagem = BytesIO()
        plt.savefig(imagem, format="png")
        plt.close()
        imagem.seek(0)
        
        return HttpResponse(imagem, content_type="image/png")
    
    @action(detail=False, methods=['GET'])
    def grafic(self, request):
        dados = Imovel.objects.values("tipo").annotate(total=Count("id"))
        
        fig, ax = plt.subplots()

        titulos = [item["tipo"] for item in dados]
        counts = [item["total"] for item in dados]
        bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

        ax.bar(titulos, counts, color=bar_colors)

        ax.set_ylabel('Títulos')
        ax.set_title('Imobiliária do Morpheu')

        imagem = BytesIO()
        plt.savefig(imagem, format="png")
        plt.close()
        imagem.seek(0)
        
        return HttpResponse(imagem, content_type="image/png")

    @action(detail=False, methods=['GET'])
    def pie(self, request):
        dados = Imovel.objects.values("tipo").annotate(total=Count("id"))

        data = [item["total"] for item in dados]
        labels = [item["tipo"] for item in dados]

        fig, ax = plt.subplots()
        pie = ax.pie(data)
        ax.pie_label(pie, labels)
        ax.pie_label(pie, '\n\n{frac:.1%}')

        imagem = BytesIO()
        plt.savefig(imagem, format="png")
        plt.close()
        imagem.seek(0)
        
        return HttpResponse(imagem, content_type="image/png")
        
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
