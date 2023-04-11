from django.urls import path

from .views import SuccessOrder, AddOrder, ContactsCreateOrderView

urlpatterns = [
    path('success/', SuccessOrder.as_view(), name='order_success'),
    path('add/', AddOrder.as_view(), name='add_order'),
    path('', ContactsCreateOrderView.as_view(), name='contacts_create_order'),
]

