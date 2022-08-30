from django.urls import include, path

from renderer import views

app_name = 'renderer'

urlpatterns = [
    path('archive', views.archive, name='archive'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
    path('collections', views.collections, name='collections'),
    path('favorites', views.favorites, name='favorites'),
]
