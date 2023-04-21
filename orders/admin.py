from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    # fields = ['created_at',]
    list_display = ('is_confirmed', 'created_at', 'name', 'contact', 'message')
    readonly_fields = ('created_at', 'name', 'contact', 'message')
    list_filter = ('is_confirmed', 'created_at')


admin.site.register(Order, OrderAdmin)
