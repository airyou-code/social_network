from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from user.models import User

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
                return HttpResponseRedirect("registrations/")
        else:
            return HttpResponseRedirect("registrations/")

    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")
