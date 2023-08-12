from django import forms


class UserForm(forms.Form):
    full_link = forms.CharField(max_length=500,
                                label='полная ссылка',
                                widget=forms.Textarea)
    short_link = forms.CharField(max_length=100,
                                 required=False,
                                 label='короткая ссылка'
                                 )
