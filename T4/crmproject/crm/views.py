from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReandonly
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CustomerViewset (ModelViewSet):
    queryset  = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

class NormalCustomerViewset (ModelViewSet):
    queryset  = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrReandonly]

