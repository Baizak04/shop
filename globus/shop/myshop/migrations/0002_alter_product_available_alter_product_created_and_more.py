# Generated by Django 4.1.7 on 2023-03-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uploaded',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменен'),
        ),
    ]
