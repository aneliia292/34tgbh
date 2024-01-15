from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
