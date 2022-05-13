from django.shortcuts import render
from django.template.defaulttags import register

def test(request):
    print('lol')


def login(request):
    return render(request, 'reg/login.html')
    pass

def logout():
    pass
