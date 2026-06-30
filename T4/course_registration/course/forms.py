from django import forms
from .models import Course

class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_code',
            'course_name',
            'description',
            'instructor',
            'duration',
            'credit'
        ]

    def clean_course_name(self):
        course_name = self.cleaned_data['course_name']
        if len(course_name)<3:
            raise forms.ValidationError('Course name must have greater than 3 letters.')
        return course_name

    def clean_duration(self):
        course_duration = self.cleaned_data['duration']
        if course_duration <= 0:
            raise forms.ValidationError('Course duretion not a 0 ')
        return course_duration


    def clean_credit(self):
        course_credit = self.cleaned_data['credit']
        if course_credit<1 or course_credit>10:
            raise forms.ValidationError('Course cradits must have beetween 1 to 10')
        
        return course_credit
    
    def clean(self):
        cleaned_data = super().clean()

        duration = self.cleaned_data['duration']
        credit = self.cleaned_data['credit']

        if duration and credit:
            if duration<credit:
                raise forms.ValidationError('sghdvfsdfjsdjf amlasdfsfn smfj')
        return cleaned_data