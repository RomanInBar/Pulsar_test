from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    CHOICE_STATUS = (
        ('ВН', 'В наличии'),
        ('ПЗ', 'Под заказ'),
        ('ОП', 'Ожидает поступления'),
        ('НН', 'Нет в наличии'),
        ('НП', 'Не производится'),
    )
    name = models.CharField(max_length=250, verbose_name='Название')
    article = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message='Значение не может быть меньше 1')
        ],
        unique=True,
        verbose_name='Артикул',
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, db_index=True, verbose_name='Цена'
    )
    status = models.CharField(
        max_length=2,
        choices=CHOICE_STATUS,
        default='ВН',
        verbose_name='Статус',
    )
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')

    class Meta:
        ordering = ('status',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} {self.article}'
