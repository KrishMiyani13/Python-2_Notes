from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Player
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import MyPagination
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
@api_view(['GET'])
def home(request):

    return Response({
        "project":"REST API Project",
        "created_by":"Prof. Pritu Patel",
        "subject":"Python Programming"
    })

class PlayerListCreate(generics.ListCreateAPIView):

    queryset = Player.objects.all()

    serializer_class = PlayerSerializer

    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
