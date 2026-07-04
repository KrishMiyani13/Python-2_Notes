from django.shortcuts import render
from rest_framework import serializers
from .serializers import ExpenseSerializers
from rest_framework.viewsets import ModelViewSet
from .models import Expense
# Create your views here.

class ExpeneViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers