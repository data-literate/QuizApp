from django.contrib.admin import register
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegistrationForm
import requests

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    resp = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple")
    #https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple
    data = resp.json()['results']
    return render(request,'index.html', {"data": data})


def register_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('login')
    else:
        form = RegistrationForm()


    """
    #for login 
    user = authenticate(request, username=username, password=password)
    if user is not None:
        register(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid register' error message.
        ...
        
    """

    return render(request, 'register.html', {'form' : form})

def logout_view(request):
    logout(request)

def quiz_view(request):
    if not request.user.is_authenticated:
        return render(request, "myapp/login_error.html")

def login_view(request):
    return HttpResponse("Login Page")
