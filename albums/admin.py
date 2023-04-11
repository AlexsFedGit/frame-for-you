from django.contrib import admin

from .models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def delete_queryset(self, request, queryset, **kwargs):
        for album in queryset:
            album.delete()


admin.site.register(Album, AlbumAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'order', 'photo', 'upload_at')


admin.site.register(Photo, PhotoAdmin)
