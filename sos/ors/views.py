from django.contrib.messages.context_processors import messages
from django.http import HttpResponse
from django.shortcuts import render

from .service.Service_user import UserService


def test_ors(request):
    return HttpResponse('<h1>welcome host</h1>')

def home_ors(request):
    return HttpResponse('<h1>welcome to home page</h1>')

def welcome(request):
    return render(request, 'welcome.html')

def user_signup(request):
    if request.method == "POST":
        form = {}
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service = UserService()
        service.add(form)
    return render(request, 'registration.html')

def user_signin(request):
    message =" "
    if request.method == "POST":
        form = {}
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')

        service = UserService()
        user_data = service.authenticate(form['login_id'], form['password'])

        if len(user_data) > 0:
            return render(request, 'welcome.html', {'firstName': user_data[0].get('first_name')})
        else:
            message = "login & password invalid"
        return render (request, 'login.html')


    return render(request, 'login.html', {'message': message})

# Create your views here.
