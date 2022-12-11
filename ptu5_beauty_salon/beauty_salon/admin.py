from django.contrib import admin
from . import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'total')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('service', 'order', 'price', 'quantity')


admin.site.register(models.Master)
admin.site.register(models.GalleryPhoto)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)

