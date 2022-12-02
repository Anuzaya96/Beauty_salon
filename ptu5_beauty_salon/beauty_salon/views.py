from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Client, Order, Service, OrderLine


def index(request):
    visits_count = request.session.get('visits_count', 1)
    request.session['visits_count'] = visits_count + 1

    return render(request, 'beauty_salon/index.html', {
        'services_count': Service.objects.count(),
        'orders_count': Order.objects.count(),
        'visits_count': visits_count,
    })

class ServiceListView(ListView):
    model = Service
    template_name = 'beauty_salon/services.html'


