import os

from django.db import models


class Album(models.Model):
    title = models.CharField(
        max_length=255
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

    def get_uniq_pair(self):
        return f'{self.pk}_{self.slug}'

    def get_absolute_url(self):
        pass

    def get_album_cover(self):
        cover = self.photo_set.all()[0]
        if cover:
            return cover.photo.url
        return 'http://127.0.0.1:8000/static/assets/img/logo.png'

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

    def save(self):
        super().save()

    class Meta:
        ordering = ['album', 'order']