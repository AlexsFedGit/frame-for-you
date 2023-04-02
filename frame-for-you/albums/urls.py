from django.urls import path

from albums.views import AlbumsList

urlpatterns = [
    path('', AlbumsList.as_view(), name='albums_list')
]