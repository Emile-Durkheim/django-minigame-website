from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Username", max_length=255,
                             widget=forms.EmailInput(attrs={'class': 'label-form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'label-form'}))