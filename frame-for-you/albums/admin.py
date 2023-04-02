from django.contrib import admin

from .models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Album, AlbumAdmin)

admin.site.register(Photo)
