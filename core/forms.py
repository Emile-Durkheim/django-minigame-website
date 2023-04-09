from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255,
                             widget=forms.EmailInput(attrs={'class': 'form-text', 
                                                            'placeholder': 'E-Mail'}))
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'form-text', 
                                                                 'placeholder': 'Passwort'}))


class RegisterForm(LoginForm):
    password2 = password