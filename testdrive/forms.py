from django import forms
from .models import TestDrive

class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = '__all__'