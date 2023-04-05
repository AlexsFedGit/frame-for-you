from django.urls import path

from . import views


urlpatterns = [
    path('call_me/', views.SendRequestView.as_view(), name='send_request'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('', views.IndexView.as_view(), name='home'),
]
