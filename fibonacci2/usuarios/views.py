from django.contrib.auth.hashers import check_password
from django.shortcuts import render

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Usuarios(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def DetalleUsuario(request, id):
    try:
        usuario = Usuario.objects.get(id = id)
    except:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def Login(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
    except:
        return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
    
    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return Response("Invalid email", status=status.HTTP_400_BAD_REQUEST)
    
    pwd_invalido = check_password(password, usuario.password)

    if not pwd_invalido:
        return Response("Invalid password", status=status.HTTP_400_BAD_REQUEST)
    
    if not usuario.is_active:
        return Response("email is not active", status=status.HTTP_400_BAD_REQUEST)
    
    token, _ = Token.objects.get_or_create(user=usuario)

    return Response(token.key, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Logout(request):
    try:
        email = request.POST.get('email')
    except:
        return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return Response("Invalid email", status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist): 
        pass

    return Response("Successfully logged out.", status=status.HTTP_200_OK)