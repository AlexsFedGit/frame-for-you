from django.views.generic import TemplateView


class ArticlesListView(TemplateView):
    template_name = 'articles/articles_list.html'
