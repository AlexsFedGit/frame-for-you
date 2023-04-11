import os
import shutil

from django.conf import settings
from django.db import models
from easy_thumbnails.files import get_thumbnailer
from slugify import slugify


class Album(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='название',
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='url',
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='создано',
    )
    last_modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='изменено',
    )

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

    def delete(self, **kwargs):
        album_dir_path = os.path.join(settings.MEDIA_ROOT, self.get_uniq_pair())
        shutil.rmtree(album_dir_path)
        super().delete(**kwargs)

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
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'


def get_upload_path(instance, filename):
    return os.path.join(instance.album.get_uniq_pair(), filename)


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='альбом',
    )
    order = models.IntegerField(
        default=0,
        verbose_name='порядок',
        blank=False,
    )
    photo = models.ImageField(
        upload_to=get_upload_path,
        verbose_name='файл',
    )
    upload_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='добавлено',
    )

    def delete(self, **kwargs):
        os.remove(get_thumbnailer(self.photo)['preview'].file.name)
        self.photo.delete()
        super().delete(**kwargs)

    def get_thumb_url(self):
        return get_thumbnailer(self.photo)['preview'].url

    def __str__(self):
        return f'{self.album.title} - {self.order}'

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
        ordering = ['album', 'order', '-upload_at']
        # unique_together = (('album', 'order'),)
