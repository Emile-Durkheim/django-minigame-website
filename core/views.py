from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'core/index.html')


def vw_login(request: HttpRequest):
    # If user is requesting site    
    if request.method == "GET":
        form = LoginForm

    # If user has submitted the form
    elif request.method == "POST":
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
    
    context = {'form': form}  # make a variable by the name of 'form' available to the login.html template; the LoginForm will be its value
    return render(request, 'core/login.html', context)


def vw_register(request: HttpRequest):
    context = {'form': RegisterForm}
    return render(request, 'core/register.html', context)