import os

from django.db import models
from easy_thumbnails.files import get_thumbnailer
from slugify import slugify


class Album(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='url'
    )
    description = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

    def get_uniq_pair(self):
        return f'{self.pk}_{self.slug}'

    def get_absolute_url(self):
        pass

    def get_album_cover_url(self):
        photos = self.photo_set.all()
        if photos:
            cover = photos[0]
            return cover.get_thumb_url()

    def get_photos_count(self):
        return len(self.photo_set.all())

    class Meta:
        ordering = ['-created_at']


def get_upload_path(instance, filename):
    return os.path.join(instance.album.get_uniq_pair(), filename)


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        default=0
    )
    photo = models.ImageField(
        upload_to=get_upload_path
    )

    def save(self, **kwargs):
        super().save(**kwargs)

    def get_thumb_url(self):
        return get_thumbnailer(self.photo)['preview'].url

    class Meta:
        ordering = ['album', 'order']



