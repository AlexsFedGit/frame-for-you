# Generated by Django 4.1.7 on 2023-04-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
