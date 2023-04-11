from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView

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


class ContactsCreateOrderView(TemplateView):
    template_name = 'orders/create_order.html'


class OrdersList(ListView):
    model = Order
    template_name = 'orders/orders_list.html'

