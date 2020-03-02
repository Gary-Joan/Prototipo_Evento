from django import forms

class PostForm(forms.Form):
    message = forms.CharField()