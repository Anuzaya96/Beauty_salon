from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from PIL import Image

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
    master = models.ForeignKey(
        User, 
        verbose_name=_("master"), 
        on_delete=models.CASCADE, 
        related_name='order_lines',
        null=True,
        blank=True
    )

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


class Master(models.Model):
    description = models.CharField(_("description"), max_length=550)
    user = models.OneToOneField(
        User, 
        verbose_name=_("master"), 
        on_delete=models.CASCADE, 
        related_name='master',
    )

    def __str__(self):
        return f"{self.user} {self.description}"


class GalleryPhoto(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    photo = models.ImageField(_("photo"), upload_to="gallery/photos")
    master = models.ForeignKey(
        User, 
        verbose_name=_("master"), 
        on_delete=models.CASCADE, 
        related_name='gallery_photos',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            dif = abs(photo.width - photo.height)
            print(dif)
            if dif:
                if photo.width > photo.height:
                    left = int(dif / 2)
                    right = photo.width - int(dif / 2)
                    top = 0
                    bottom = photo.height
                else:
                    left = 0
                    right = photo.width
                    top = int(dif / 2)
                    bottom = photo.height - int(dif / 2)
                box = (left, top, right, bottom)
                print(box)
                photo = photo.crop(box)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
            photo.save(self.photo.path)


    def __str__(self):
        return self.photo.url    

    class Meta:
        ordering = ('master', '-created_at')








