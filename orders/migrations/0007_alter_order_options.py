# Generated by Django 4.1.7 on 2023-04-21 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['is_confirmed', '-created_at'], 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
    ]
