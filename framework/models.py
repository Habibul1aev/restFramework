from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Фото', upload_to='media/')
    discription = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0.0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product', verbose_name='Категория')
    tags = models.ManyToManyField('Tags', related_name='product', verbose_name='Теги')
    created_date = models.TimeField("Создан", auto_now_add=True)
    update_date = models.TimeField("Изменен", auto_now=True)
    is_publish = models.BooleanField('Публичность')

    def __str__(self):
        return self.title
    
    

class Category(models.Model):
    title = models.CharField("Категория", max_length=50)

    def __str__(self) -> str:
        return self.title
    
class Tags(models.Model):
    tag = models.CharField("Теги", max_length=50)

    def __str__(self) -> str:
        return self.tag