from django.urls import include, path

from view import views

app_name = 'view'

urlpatterns = [
    # Entry point
    path('dashboard', views.dashboard, name='dashboard'),

    path('archive', views.archive, name='archive'),
    path('favorites', views.favorites, name='favorites'),
    path('library', views.library, name='library'),
]
