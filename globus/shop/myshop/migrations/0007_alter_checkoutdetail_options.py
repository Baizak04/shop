# Generated by Django 4.1.7 on 2023-04-08 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_remove_checkoutdetail_customer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkoutdetail',
            options={'ordering': ('name',), 'verbose_name': 'Оформления заказа', 'verbose_name_plural': 'Оформления заказа'},
        ),
    ]
