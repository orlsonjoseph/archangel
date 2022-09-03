from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from bookmark import views

app_name = 'api'

urlpatterns = [
    path('auth/token', obtain_auth_token, name='api-token'),

    path('bookmark/create', views.create_bookmark_instance, name='create_boomark'),
    path('bookmark/is-bookmarked', views.is_page_bookmarked,
         name='is_page_bookmarked'),
    path('bookmark/search', views.search_bookmarks, name='search_bookmarks'),
]
