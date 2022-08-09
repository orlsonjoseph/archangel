from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from bookmark import views

app_name = 'api'

urlpatterns = [
    path('auth/token', obtain_auth_token, name='api-token'),

    path('bookmark/create', views.create_bookmark_instance, name='create_boomark')
]