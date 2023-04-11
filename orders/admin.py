from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    # fields = ['created_at',]
    list_display = ('created_at', 'name', 'contact', 'message', 'is_confirmed')
    readonly_fields = ('created_at', 'name', 'contact', 'message')
    list_filter = ('is_confirmed', 'created_at')


admin.site.register(Order, OrderAdmin)
