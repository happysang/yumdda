from django import forms
from django.forms import fields
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','writer','body','image']