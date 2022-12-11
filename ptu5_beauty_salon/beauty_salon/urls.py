from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.ServiceListView.as_view(), name='salon_services'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('gallery/', views.gallery, name='gallery')
    # path('add_an_order/', views.UserOrderCreateView.as_view(), name='user_create_an_order'),
]