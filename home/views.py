from django.views.generic import TemplateView

from orders.models import Order


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders_count = len(Order.objects.filter(is_confirmed=False))
        context['orders_count'] = orders_count
        return context
