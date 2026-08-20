from django.urls import path
from .views_generics import *

urlpatterns = [
    path("usuarios/", UsuarioListCreateAPIView.as_view(), name="usuarios-list-create"),
    path("usuarios/<int:pk>/", UsuarioRetrieveUpdateDestroyAPIView.as_view(), name="usuarios-detail"),

    path("imoveis/", ImovelListCreateAPIView.as_view(), name="imoveis-list-create"),
    path("imoveis/<int:pk>/", ImovelRetrieveUpdateDestroyAPIView.as_view(), name="imoveis-detail"),

    path("contratos/", ContratoListCreateAPIView.as_view(), name="contratos-list-create"),
    path("contratos/<int:pk>/", ContratoRetrieveUpdateDestroyAPIView.as_view(), name="contratos-detail"),

    path("pagamentos/", PagamentoListCreateAPIView.as_view(), name="pagamentos-list-create"),
    path("pagamentos/<int:pk>/", PagamentoRetrieveUpdateDestroyAPIView.as_view(), name="pagamentos-detail"),
]