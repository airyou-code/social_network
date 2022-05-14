from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponseRedirect
from user.models import User

import random
import string

def test(request):
    print('lol')

def singIn(request):
    if request.method == "POST":
        user = User()
        user.mail = request.POST.get("mail")
        print(request.POST.get("mail"))
        user.password = request.POST.get("password")
        user.login = request.POST.get("login")
        token = random_token(20)
        user.token = token
        user.description = ""
        user.save()
        response = HttpResponseRedirect(f"/{user.id}")
        response.set_cookie('user_id', user.id)
        response.set_cookie('token', token)
        return response

    return render(request, 'reg/singin.html')

def logout(request):
    pass

def newUser(request):
    pass

def random_token(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
