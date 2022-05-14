from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from user.models import User
import random
import string

def index(request):
    
    return render(request, 'main/index.html')


def ls(request, pk):
    try:
        user = User.objects.get(id=pk)
        if 'token' in request.COOKIES:
            token = request.COOKIES['token']
            if token == user.token:
                return render(request, "main/index.html", {"user": user})
            else:
                response = HttpResponseRedirect(f"/login")
                response.delete_cookie('token')
                response.delete_cookie('user_id')
                return response
        else:
            response = HttpResponseRedirect(f"/login")
            response.delete_cookie('token')
            response.delete_cookie('user_id')
            return response

    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")


def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(login=request.POST.get("login"))
            if user.password == request.POST.get("password"):
                token = random_token(20)
                user.token = token
                user.save()
                response = HttpResponseRedirect(f"/{user.id}")
                response.set_cookie('token', token)
                response.set_cookie('user_id', user.id)
                return response
                pass

        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>user not found</h2>")
    else:
        return render(request, 'reg/login.html')
    pass

def logout(request):
    response = HttpResponseRedirect(f"/login")
    response.delete_cookie('token')
    response.delete_cookie('user_id')
    return response
    pass

def edit(request):
    if request.method == "POST":
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])
            if user.token == request.COOKIES['token']:
                token = random_token(20)
                user.token = token
                user.login = request.POST.get("login")
                user.description = request.POST.get("description")
                user.save()
                response = HttpResponseRedirect(f"/{user.id}")
                response.set_cookie('token', token)
                response.set_cookie('user_id', user.id)
                return response
                pass

        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>user not found</h2>")
    else:
        return render(request, 'main/edit.html')
    pass
    pass

def random_token(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
