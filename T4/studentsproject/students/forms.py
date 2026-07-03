from django import forms
from .models import Student,Course

class StudentForm(forms.ModelForm):
    Course = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    class Meta:
        model = Student
        fields = ['name', 'email', 'enrollment_number', 'phn_number','Course']


