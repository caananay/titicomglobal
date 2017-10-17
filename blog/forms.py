from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(label='From', max_length=25, widget=forms.HiddenInput())
    email = forms.EmailField(widget=forms.HiddenInput())
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)