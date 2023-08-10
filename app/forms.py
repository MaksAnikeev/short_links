from django import forms
class UserForm(forms.Form):
    full_link = forms.CharField(max_length=500)
    short_link = forms.CharField(max_length=100, required=False)
