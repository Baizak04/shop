# Generated by Django 4.1.7 on 2023-04-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_order_delete_checkoutdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mbank_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
