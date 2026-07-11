from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False,methods=['GET'])
    def top(self,request):
        movies = Movie.objects.filter(rating__gt = 8)
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    @action(detail=False,methods=['GET'])
    def buttom(self,request):
        movies = Movie.objects.filter(rating__lt = 8)
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)