from django.shortcuts import render
from django.views.generic import TemplateView


class AlbumsList(TemplateView):
    template_name = 'albums/albums_list.html'
