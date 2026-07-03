from rest_framework import serializers
from .models import Student,Course

class CouresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','code']
        
class StudentSerializers(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset = Course.objects.all(),many=True)
    class Meta:
        model = Student
        fields = ['name','email','enrollment','phn_number','course']

