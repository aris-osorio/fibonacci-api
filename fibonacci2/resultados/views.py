from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from resultados.models import Resultado
from resultados.serializers import ResultadoSerializer
from resolver.resolver import Resolver

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Resultados(request):
    if request.method == 'GET':
        resultados = Resultado.objects.all()
        serializer = ResultadoSerializer(resultados, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        secuencia = ' '

        try:
            numero_entrada = int(request.POST.get('numero_entrada'))
        except:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        
        if numero_entrada < 0:
            return Response("Invalid data: only positive numbers", status=status.HTTP_400_BAD_REQUEST)
        
        fibonacci = Resolver.fibonacci(numero_entrada)
            
        for elemento in fibonacci:
            secuencia += str(elemento)+' ' 
        
        serializer = ResultadoSerializer(data = {
            'numero_entrada': numero_entrada,
            'secuencia': secuencia
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def DetalleResultado(request, id):
    try:
        resultado = Resultado.objects.get(id = id)
    except:
        return Response("Resultado not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResultadoSerializer(resultado)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ResultadoSerializer(resultado, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        resultado.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)