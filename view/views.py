from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.templatetags.static import static

from bookmark.models import BookmarkInstance

# Create your views here.


@login_required
def dashboard(request, template='dashboard.html'):
    return render(request, template)


@login_required
def library(request, template='include/views/library.html'):
    if request.is_ajax():
        bookmarks = request.user.saved_bookmarks.all()
        content = loader.get_template(template)
        context = {
            'svg': static('archangel/img/undraw_library.svg'),
            'message': 'Add a bookmark using the nodraft extension',

            'bookmark_list': bookmarks,
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
