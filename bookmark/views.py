from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from bookmark.models import BookmarkInstance


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_bookmark_instance(request, format=None):
    url, title, favicon_url = request.data.values()

    instance = BookmarkInstance(user=request.user)
    created = instance.save(url)

    if created:
        instance.bookmark.title = title

        if favicon_url:
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
