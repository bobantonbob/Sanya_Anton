from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'subject', 'message']

