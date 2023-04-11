# Generated by Django 4.1.7 on 2023-04-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.CharField(max_length=100, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='Заказ выполнен'),
        ),
        migrations.AlterField(
            model_name='order',
            name='message',
            field=models.TextField(blank=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
