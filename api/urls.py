from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from .importar import *

router = DefaultRouter()

router.register("usuarios", UsuarioViewSet, basename="usuarios")
router.register("imoveis", ImovelViewSet, basename="imoveis")
router.register("contratos", ContratoViewSet, basename="contratos")
router.register("pagamentos", PagamentoViewSet, basename="pagamentos")


urlpatterns = [
    path('importar_usuarios/', ImportarUsuarios.as_view()),
    path('importar_imoveis/', ImportarImoveis.as_view()),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("", include(router.urls)),
]