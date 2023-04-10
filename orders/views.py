from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import View, TemplateView

from .services import *


class AddOrder(View):
    """Создание нового заказа"""
    def post(self, request):
        try:
            create_order(request.POST.get('name'), request.POST.get('contacts'), request.POST.get('message'))
        except ValueError:
            return HttpResponse('Ошибка отправки запроса', status=500)
        return HttpResponseRedirect(reverse('order_success'))


class SuccessOrder(TemplateView):
    template_name = "orders/success.html"
    # url = reverse('home')
