from django.shortcuts import render
from django.views.generic import ListView, DetailView

from albums.models import Album


class AlbumsList(ListView):
    model = Album
    paginate_by = 20
    template_name = 'albums/templates/albums/albums_list.html'
    context_object_name = 'albums'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AlbumDetail(DetailView):
    model = Album
    template_name = 'albums/templates/albums/album_detail.html'
    context_object_name = 'album'
