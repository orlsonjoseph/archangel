from django.urls import include, path

from core import views

app_name = 'core'

urlpatterns = [
    # landing specified in archangel.urls

    path('connect', views.connect, name='connect'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
