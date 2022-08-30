from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

# Create your views here.


@login_required
def bookmarks(request, template='bookmarks.html'):
    saved_bookmarks = request.user.saved_bookmarks.all()
    return render(request, template, {
        'bookmarks': saved_bookmarks,

        # ER empty_resource
        'ER_svg': static('archangel/img/undraw_bookmarks.svg'),
        'ER_message': 'Add a bookmark using the nodraft extension'
    })


@login_required
def collections(request, template='collections.html'):
    saved_bookmarks = request.user.saved_bookmarks.all()
    return render(request, template, {
        'collections': saved_bookmarks,

        # ER empty_resource
        'ER_svg': static('archangel/img/undraw_collections.svg'),
        'ER_message': 'Organize your bookmarks in relevant collections'
    })


@login_required
def favorites(request, template='favorites.html'):
    saved_bookmarks = request.user.saved_bookmarks.all()
    return render(request, template, {
        'favorites': saved_bookmarks,

        # ER empty_resource
        'ER_svg': static('archangel/img/undraw_favorites.svg'),
        'ER_message': 'Favorite your priority bookmarks for easy access'
    })


@login_required
def archive(request, template='archive.html'):
    saved_bookmarks = request.user.saved_bookmarks.all()
    return render(request, template, {
        'archives': saved_bookmarks,

        # ER empty_resource
        'ER_svg': static('archangel/img/undraw_archive.svg'),
        'ER_message': 'Archive your unused bookmark to sort out the clutter'
    })
