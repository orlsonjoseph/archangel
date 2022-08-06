from django.urls import include, path

from core import views

app_name = 'core'

urlpatterns = [
    path('connect', views.connect, name='connect'),
    path('landing', views.landing, name='landing'),
    path('login', views.login, name='login'),
]