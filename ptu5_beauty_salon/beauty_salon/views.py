from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Client, Order, Service, OrderLine
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


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


class OrderDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'beauty_salon/order_detail.html'

    def test_func(self):
        return self.get_object().client == self.request.user.client


# class UserOrderCreateView(LoginRequiredMixin, CreateView):
#     model = OrderLine
#     fields = ('service', 'master')
#     template_name  = 'beauty_salon/user_create_order.html'
#     success_url = reverse_lazy('user_orders')

#     def form_valid(self, form):
#         form.instance.price = form.instance.service.price
#         return super().form_valid(form)
