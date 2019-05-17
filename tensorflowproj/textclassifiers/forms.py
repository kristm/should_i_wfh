from django import forms

class ClassifyForm(forms.Form):
    post = forms.CharField()