from rest_framework import serializers
from .models import Course,Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','code']

class StudentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),many=True)
    class Meta:
        model = Student
        fields = ['id','name','email','enrollnment_number','phn_number','course']
