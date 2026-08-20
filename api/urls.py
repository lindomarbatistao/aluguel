from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views_apiview import *
from .views_generics import *
from .views_viewset import *


router = DefaultRouter()

router.register("usuarios", UsuarioViewSet, basename="usuarios")
router.register("imoveis", ImovelViewSet, basename="imoveis")
router.register("contratos", ContratoViewSet, basename="contratos")
router.register("pagamentos", PagamentoViewSet, basename="pagamentos")


urlpatterns = [
    path("apiview/usuarios/", UsuarioAPIView.as_view(), name="apiview-usuarios"),
    path("apiview/usuarios/<int:pk>/", UsuarioDetailAPIView.as_view(), name="apiview-usuario-detail"),

    path("apiview/imoveis/", ImovelAPIView.as_view(), name="apiview-imoveis"),
    path("apiview/imoveis/<int:pk>/", ImovelDetailAPIView.as_view(), name="apiview-imovel-detail"),

    path("apiview/contratos/", ContratoAPIView.as_view(), name="apiview-contratos"),
    path("apiview/contratos/<int:pk>/", ContratoDetailAPIView.as_view(), name="apiview-contrato-detail"),

    path("apiview/pagamentos/", PagamentoAPIView.as_view(), name="apiview-pagamentos"),
    path("apiview/pagamentos/<int:pk>/", PagamentoDetailAPIView.as_view(), name="apiview-pagamento-detail"),

    path("generics/usuarios/", UsuarioListCreateAPIView.as_view(), name="generics-usuarios"),
    path("generics/usuarios/<int:pk>/", UsuarioRetrieveUpdateDestroyAPIView.as_view(), name="generics-usuario-detail"),

    path("generics/imoveis/", ImovelListCreateAPIView.as_view(), name="generics-imoveis"),
    path("generics/imoveis/<int:pk>/", ImovelRetrieveUpdateDestroyAPIView.as_view(), name="generics-imovel-detail"),

    path("generics/contratos/", ContratoListCreateAPIView.as_view(), name="generics-contratos"),
    path("generics/contratos/<int:pk>/", ContratoRetrieveUpdateDestroyAPIView.as_view(), name="generics-contrato-detail"),

    path("generics/pagamentos/", PagamentoListCreateAPIView.as_view(), name="generics-pagamentos"),
    path("generics/pagamentos/<int:pk>/", PagamentoRetrieveUpdateDestroyAPIView.as_view(), name="generics-pagamento-detail"),

    path("viewset/", include(router.urls)),
]