from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token


def landing(request, template='landing.html'):
    return render(request, template)


def register(request, template='register.html'):
    if request.user.is_authenticated:
        return redirect('view:dashboard')

    return render(request, template)


def login(request, template='login.html'):
    if request.user.is_authenticated:
        return redirect('view:dashboard')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('view:dashboard')
        else:
            return render(request, template)

    return render(request, template)


@login_required
def logout(request, template=None):
    django_logout(request)
    return redirect("landing")


@login_required
def connect(request, template='connect.html'):
    user_token = Token.objects.get(user=request.user)
    return render(request, template, {
        'token': user_token,
    })
