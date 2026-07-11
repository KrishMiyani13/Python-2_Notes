from django.shortcuts import render
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.

@api_view(["GET"])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message':"this is used for public access"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({'message':"this is used for private access"})
=======

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'Message':"This is used for public access. "})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def privet_view(request):
    return Response({'Message': "This is used for private access."})
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2
