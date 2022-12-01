from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'beauty_salon/index.html', {
        'services_count': models.Service.objects.count(),
        'orders_count': models.Order.objects.count(), 
    })

