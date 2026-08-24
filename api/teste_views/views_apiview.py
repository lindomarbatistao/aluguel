from django.shortcuts import render
from rest_framework.decorators import api_view
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UsuarioAPIView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioDetailAPIView(APIView):
    def get_object(self, pk):
        return Usuario.objects.get(pk=pk)
    
    def get(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ImovelAPIView(APIView):
    def get(self, request):
        imoveis = Imovel.objects.all()
        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ImovelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImovelDetailAPIView(APIView):
    def get_object(self, pk):
        return Imovel.objects.get(pk=pk)
    
    def get(self, request, pk):
        imoveis = self.get_object(pk)
        serializer = ImovelSerializer(imoveis)
        return Response(serializer.data)
    
    def put(self, request, pk):
        imoveis = self.get_object(pk)
        serializer = ImovelSerializer(imoveis, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        imoveis = self.get_object(pk)
        imoveis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContratoAPIView(APIView):
    def get(self, request):
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContratoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContratoDetailAPIView(APIView):
    def get_object(self, pk):
        return Contrato.objects.get(pk=pk)
    
    def get(self, request, pk):
        contrato = self.get_object(pk)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
    
    def put(self, request, pk):
        contrato = self.get_object(pk)
        serializer = ContratoSerializer(contrato, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        contrato = self.get_object(pk)
        contrato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PagamentoAPIView(APIView):
    def get(self, request):
        pagamentos = Pagamento.objects.all()
        serializer = PagamentoSerializer(pagamentos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PagamentoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PagamentoDetailAPIView(APIView):
    def get_object(self, pk):
        return Pagamento.objects.get(pk=pk)
    
    def get(self, request, pk):
        pagamento = self.get_object(pk)
        serializer = PagamentoSerializer(pagamento)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pagamento = self.get_object(pk)
        serializer = PagamentoSerializer(pagamento, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pagamento = self.get_object(pk)
        pagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    