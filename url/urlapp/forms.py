from django import forms

class Url(forms.Form):
    l_url = forms.CharField(label="l_url")
