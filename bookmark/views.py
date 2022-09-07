from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.templatetags.static import static

from bookmark.models import BookmarkInstance


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_bookmark_instance(request, format=None):
    url, title, favicon_url = request.data.values()

    instance = BookmarkInstance(user=request.user, title=title)
    created = instance.save(url)

    if created and favicon_url:
        instance.bookmark.has_favicon = True
        instance.bookmark.favicon_url = favicon_url

        instance.bookmark.save()

    return Response({
        "message": "bookmark instance created"
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def is_page_bookmarked(request, format=None):
    return Response({
        'bookmarked': False,
    })


def show_bookmark_instance(request, pk, format=None):
    bookmark = get_object_or_404(
        BookmarkInstance, pk=pk, user=request.user)

    return JsonResponse(serializers.serialize('json', [bookmark]), safe=False)


def edit_bookmark(request, template=None):
    if request.is_ajax() and request.method == 'POST':
        bookmark_id = request.POST.get('bookmark_id', None)

        if bookmark_id is None:
            return HttpResponse('Bookmark id is required', status=400)

        bookmark = BookmarkInstance.objects.get(
            user=request.user, id=bookmark_id)

        print(bookmark)

        return JsonResponse(data=context, status=200)
    return JsonResponse(data={}, status=400)


def search_bookmarks(request, template='include/views/search.html'):
    content, context = loader.get_template(template), {}

    if request.is_ajax() and request.method == 'GET':
        query = request.GET.get('query', None)

        if query is None:
            return HttpResponse('Query is required', status=400)

        bookmarks = BookmarkInstance.objects.filter(
            user=request.user, bookmark__title__icontains=query)

        if bookmarks:
            context["bookmark_list"] = bookmarks

        return HttpResponse(content.render(context, request), status=200)
    return HttpResponse('Bad request', status=400)
