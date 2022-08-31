from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.templatetags.static import static

# Create your views here.


@login_required
def dashboard(request, template='dashboard.html'):
    return render(request, template)


@login_required
def bookmarks(request, template='include/views/bookmarks.html'):
    if request.is_ajax():
        bookmarks = ["Hello", "Darkness", "My", "Old", "Friend", "I", "Wanted"]
        content = loader.get_template(template)
        context = {
            'svg': static('archangel/img/undraw_bookmarks.svg'),
            'message': 'Add a bookmark using the nodraft extension',

            'bookmarks': bookmarks,
        }
        return HttpResponse(content.render(context, request))
    return HttpResponse('Bad request')


@login_required
def collections(request, template='include/views/collections.html'):
    if request.is_ajax():
        content = loader.get_template(template)
        context = {
            'svg': static('archangel/img/undraw_collections.svg'),
            'message': 'Organize your bookmarks in relevant collections'
        }
        return HttpResponse(content.render(context, request))
    return HttpResponse('Bad request')


@login_required
def favorites(request, template='include/views/favorites.html'):
    if request.is_ajax():
        content = loader.get_template(template)
        context = {
            'svg': static('archangel/img/undraw_favorites.svg'),
            'message': 'Favorite your priority bookmarks for easy access'
        }
        return HttpResponse(content.render(context, request))
    return HttpResponse('Bad request')


@login_required
def archive(request, template='include/views/archive.html'):
    if request.is_ajax():
        content = loader.get_template(template)
        context = {
            'svg': static('archangel/img/undraw_archive.svg'),
            'message': 'Archive your unused bookmark to sort out the clutter'
        }
        return HttpResponse(content.render(context, request))
    return HttpResponse('Bad request')
