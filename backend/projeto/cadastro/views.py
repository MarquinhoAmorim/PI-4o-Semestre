from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import usuario
from .serializers import usuarioSerializer

# Create your views here.

def home(request):
    return render(request, 'home/index.html', {'user': request.user})

@api_view(['GET'])
def get_usuarios(request):
    
    if request.method == 'GET':
        
        users = usuario.objects.all()
        serializer = usuarioSerializer(users, many=True)
        print(serializer.data[0]['nome'])
        return Response(serializer.data)
        

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_usuarios(request):
    
    if request.method == 'POST':
        
        user = usuarioSerializer(data = request.data)
        user.is_valid(raise_exception=True)
        user.save
        print(user.data[0]['nome'])
        return Response(user.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)