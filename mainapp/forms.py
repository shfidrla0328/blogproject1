from django import forms
from .models import Blog

class CreatePost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']