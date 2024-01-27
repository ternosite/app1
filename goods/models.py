from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='url')

    class Meta:
        db_table='category'
        verbose_name='Категорию'
        verbose_name_plural='Категории'
        
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='url')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    categorie = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='категория')
    
    
    class Meta:
        db_table='product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        
    def __str__(self):
        return f'{self.name}, в наличии {self.quantity}'    
