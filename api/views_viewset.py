from rest_framework.viewsets import ModelViewSet
from .models import (Usuario, Imovel, Contrato, Pagamento)
from .serializers import (UsuarioSerializer, ImovelSerializer,
    ContratoSerializer, PagamentoSerializer)

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer