from .models import Order


def create_order(name: str, contact: str, message: str):
    if not name:
        raise ValueError
    if not contact:
        raise ValueError
    order = Order.objects.create()
    order.name = name
    order.contact = contact
    order.message = message
    order.save()

