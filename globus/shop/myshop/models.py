from django.urls import reverse
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    """_summary_

    Returns:
        _type_: _description_
    """
    """_summary_

    Returns:
        _type_: _description_
    """
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
      
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])
    



class Order(models.Model):
    email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    mbank_number = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=100, blank=True)
    total_price = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.email
