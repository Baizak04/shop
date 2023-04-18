# Generated by Django 4.1.7 on 2023-04-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_alter_checkoutdetail_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.IntegerField(max_length=100)),
                ('mbank_number', models.IntegerField(blank=True, max_length=100)),
                ('total_price', models.CharField(blank=True, max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.product')),
            ],
        ),
        migrations.DeleteModel(
            name='CheckoutDetail',
        ),
    ]
