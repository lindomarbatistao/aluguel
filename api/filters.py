import django_filters
from .models import Usuario, Pagamento, Contrato, Imovel

# gt            >
# gte           >=
# lt            <
# lte           <=
# contains      contém
# icontains     contém, ignorando maiúscula/minúscula
# exact         =   
# iexact        =   (ignorando maiúscula/minúscula)

class UsuarioFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(field_name="tipo", lookup_expr="exact")
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    
    class Meta:
        model = Usuario
        fields = ["tipo", "first_name"]
        
class ImovelFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name="titulo", lookup_expr="icontains")
    tipo = django_filters.CharFilter(field_name="tipo", lookup_expr="icontains")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    valor_aluguel = django_filters.CharFilter(field_name="valor_aluguel", lookup_expr="gt")
    
    class Meta:
        model = Imovel
        fields = ["titulo", "tipo", "status", "valor_aluguel"]

class ContratoFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name="data_inicio", lookup_expr="gte")
    data_fim = django_filters.DateFilter(field_name="data_fim", lookup_expr="lte")
    valor_min = django_filters.NumberFilter(field_name="valor", lookup_expr="gte")
    valor_max = django_filters.NumberFilter(field_name="valor", lookup_expr="lte")
    locador = django_filters.NumberFilter(field_name="locador_id")
    
    class Meta:
        model = Contrato
        fields = ["data_inicio", "data_fim", "valor_min", "valor_max", "locador"]
    
class PagamentoFilter(django_filters.FilterSet):
    data_pagamento = django_filters.DateFilter(field_name="data_pagamento")
    status = django_filters.BooleanFilter(field_name="status")
    
    class Meta:
        model = Pagamento
        fields = ["data_pagamento", "status"]