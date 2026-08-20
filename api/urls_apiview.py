from rest_framework.urls import path
from .views_apiview import *

urlpatterns = [
    path('usuarios', UsuarioAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailAPIView.as_view()),
    
    path('imoveis', ImovelAPIView.as_view()),
    path('imovel/<int:pk>', ImovelDetailAPIView.as_view()),
    
    path('contratos', ContratoAPIView.as_view()),
    path('contrato/<int:pk>', ContratoDetailAPIView.as_view()),
    
    path('pagamentos', PagamentoAPIView.as_view()),
    path('pagamento/<int:pk>', PagamentoDetailAPIView.as_view())
]
