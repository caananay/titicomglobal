from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'body')
        widgets ={'name':forms.HiddenInput(), 'email':forms.HiddenInput()}