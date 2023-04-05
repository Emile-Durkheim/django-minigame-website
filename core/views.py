from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest
from django.contrib.auth import authenticate, login, logout

from .django_forms import LoginForm

# Create your views here.
def login(request: HttpRequest):
    context = {'form': LoginForm}

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                context['message'] = "Login erfolgreich"
            else:
                context['message'] = "E-Mail oder Passwort falsch"
        
        else:
            context['message'] = "Login fehlgeschlagen"
            context['errors'] = str(form.errors)
    
    return render(request, 'core/login.html', context)