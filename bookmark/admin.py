from django.contrib import admin

from bookmark.models import Bookmark, BookmarkInstance

admin.site.register(Bookmark)
admin.site.register(BookmarkInstance)
