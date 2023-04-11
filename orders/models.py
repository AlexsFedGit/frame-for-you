from django.db import models


class Order(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )
    contact = models.CharField(
        max_length=100,
        verbose_name='Контакты',
    )
    message = models.TextField(
        blank=True,
        verbose_name='Сообщение'
    )
    is_confirmed = models.BooleanField(
        default=False,
        verbose_name='Заказ выполнен'
    )

    def __str__(self):
        return f'{self.name} - {self.contact}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['-created_at']
