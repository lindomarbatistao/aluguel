import django_filters
from .models import Usuario, Pagamento, Contrato, Imovel

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    tipo = django_filters.CharFilter(field_name="tipo", lookup_expr="exact")
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    
    class Meta:
        model = Usuario
        fields = ["tipo", "first_name"]
        
class ImovelFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name="titulo", lookup_expr="icontains")
    tipo = django_filters.CharFilter(field_name="tipo", lookup_expr="icontains")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    
    class Meta:
        model = Imovel
        fields = ["titulo", "tipo", "status"]
