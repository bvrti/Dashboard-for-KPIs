from django import forms
from .models import *

class Photo1(forms.ModelForm):
    class Meta:
        fields = ('image')

class Photo2(forms.ModelForm):
    class Meta:
        fields = ('image')

class Photo3(forms.ModelForm):
    class Meta:
        fields = ('image')

class Photo4(forms.ModelForm):
    class Meta:
        fields = ('image')

class Photo5(forms.ModelForm):
    class Meta:
        fields = ('image')

class Photo6(forms.ModelForm):
    class Meta:
        fields = ('image')
