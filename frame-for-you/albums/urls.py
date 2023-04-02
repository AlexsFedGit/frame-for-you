from django.urls import path

from albums.views import AlbumsList, AlbumDetail

urlpatterns = [
    path('', AlbumsList.as_view(), name='albums_list'),
    path('<int:id>_<slug:slug>/', AlbumDetail.as_view(), name='album_detail'),
]
