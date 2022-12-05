from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Client, Order, Service, OrderLine
from django.views.generic.edit import FormMixin


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


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'beauty_salon/order_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if hasattr(self.request.user, 'client'): 
            queryset = queryset.filter(client=self.request.user.client).order_by('-date')
        else:
            queryset = None
        return queryset


class OrderDetailView(FormMixin, DetailView):
    model = Order
    template_name = 'beauty_salon/order_detail.html'
