from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'


class SendRequestView(TemplateView):
    template_name = 'home/send_request.html'


class ContactsView(TemplateView):
    template_name = 'home/contacts.html'
