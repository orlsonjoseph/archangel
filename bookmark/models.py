from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime

# Create your models here.

CustomUser = get_user_model()


class Bookmark(models.Model):
    url = models.URLField(unique=True)

    has_favicon = models.BooleanField(default=False)
    favicon_checked = models.DateTimeField(default=datetime.now)

    description = models.CharField(max_length=100)

    added = models.DateTimeField(default=datetime.now)

    def get_favicon_url(force=False):
        return None

    def __str__(self) -> str:
        return self.url

    class Meta:
        ordering = ('-added', )


class BookmarkInstance(models.Model):
    bookmark = models.ForeignKey(
        Bookmark, related_name='saved_instances', verbose_name='bookmark', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='saved_bookmarks',
                             verbose_name='user', on_delete=models.CASCADE)

    note = models.TextField(blank=True)

    saved = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(default=datetime.now)

    def save(self, force_insert=False, force_update=False):
        bookmark, created = Bookmark.objects.get_or_create(url=self.url)
        self.bookmark = bookmark

        super(BookmarkInstance, self).save(force_insert, force_update)

    def delete(self):
        bookmark = self.bookmark
        super(BookmarkInstance, self).delete()

        if bookmark.saved_instances.all().count() == 0:
            bookmark.delete()

    def __str__(self) -> str:
        return f"{self.bookmark} for {self.user}"

    class Meta:
        ordering = ('-saved', )
