from rest_framework import serializers
from .models import Usuario, Imovel, Pagamento, Contrato

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email", 
            "celular",
            "password"
        ]
        
        extra_kwargs = {
            "password":{"write_only": True}
        }
        
    def create(self, validate_data):
        password = validate_data.pop("password")
        usuario = Usuario(**validate_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'