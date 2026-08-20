from rest_framework.routers import DefaultRouter

from .views_viewset import (
    UsuarioViewSet,
    ImovelViewSet,
    ContratoViewSet,
    PagamentoViewSet
)

router = DefaultRouter()

router.register("usuarios",UsuarioViewSet,basename="usuarios")
router.register("imoveis",ImovelViewSet,basename="imoveis")
router.register("contratos",ContratoViewSet,basename="contratos")
router.register("pagamentos",PagamentoViewSet,basename="pagamentos")

urlpatterns = router.urls