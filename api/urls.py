from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views_viewset import *

router = DefaultRouter()

router.register("usuarios", UsuarioViewSet, basename="usuarios")
router.register("imoveis", ImovelViewSet, basename="imoveis")
router.register("contratos", ContratoViewSet, basename="contratos")
router.register("pagamentos", PagamentoViewSet, basename="pagamentos")


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("viewset/", include(router.urls)),
]