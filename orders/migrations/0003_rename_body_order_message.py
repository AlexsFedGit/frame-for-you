# Generated by Django 4.1.7 on 2023-04-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_is_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='body',
            new_name='message',
        ),
    ]