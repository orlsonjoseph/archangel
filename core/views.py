from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


def landing(request, template='landing.html'):
    return render(request, template)


def register(request, template='register.html'):
    return render(request, template)


def login(request, template='login.html'):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            return redirect('core:connect')
        else:
            return render(request, template)

    return render(request, template)


@login_required
def connect(request, template='connect.html'):
    user_token = Token.objects.get(user=request.user)
    return render(request, template, {
        'token': user_token,
    })
