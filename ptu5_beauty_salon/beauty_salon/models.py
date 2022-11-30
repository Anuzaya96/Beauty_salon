from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Client(models.Model):
    phone = models.CharField(_("phone"), max_length=20)
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE, 
        related_name="client"
    )

    def __str__(self) -> str:
        return f"{self.phone} {self.user}"


class Order(models.Model):
    date = models.DateField(_("date"), auto_now_add=True)
    total = models.DecimalField(_("total amount"), max_digits=18, decimal_places=2, default=0)
    client = models.ForeignKey(
        Client,
        verbose_name=_("client"),
        on_delete=models.CASCADE,
        related_name='orders'
    )

    def __str__(self) -> str:
        return f"{self.id} {self.date} {self.total}"


class Service(models.Model):
    name = models.CharField(_("name"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=18, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"{self.name} {self.price}"


class OrderLine(models.Model):
    quantity = models.IntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), max_digits=18, decimal_places=2)
    order = models.ForeignKey(
        Order,
        verbose_name=_("order"),
        on_delete=models.CASCADE,
        related_name="order_lines"
    )

    service = models.ForeignKey(
        Service,
        verbose_name=_("service"),
        on_delete=models.CASCADE,
        related_name="order_lines"
    )
    
    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"{self.service} {self.quantity} {self.price}"








