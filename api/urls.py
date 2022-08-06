from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    
    path('auth/token', obtain_auth_token, name='api-token'),
]