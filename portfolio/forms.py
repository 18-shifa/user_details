from django import forms
from .models import WorkExperience, Education, Certification

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
