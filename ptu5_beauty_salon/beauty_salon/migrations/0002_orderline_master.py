# Generated by Django 4.1.3 on 2022-12-02 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beauty_salon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to=settings.AUTH_USER_MODEL, verbose_name='master'),
        ),
    ]