from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from ..models import (
    Usuario,
    Imovel,
    Contrato,
    Pagamento
)

from ..serializers import (
    UsuarioSerializer,
    ImovelSerializer,
    ContratoSerializer,
    PagamentoSerializer
)


# -------------------------
# USUARIO
# -------------------------

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# -------------------------
# IMOVEL
# -------------------------

class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


class ImovelRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


# -------------------------
# CONTRATO
# -------------------------

class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


class ContratoRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


# -------------------------
# PAGAMENTO
# -------------------------

class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer


class PagamentoRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer