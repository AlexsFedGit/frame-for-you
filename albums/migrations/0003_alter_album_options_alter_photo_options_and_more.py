# Generated by Django 4.1.7 on 2023-04-11 09:15

import albums.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_photo_options_photo_upload_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-created_at'], 'verbose_name': 'альбом', 'verbose_name_plural': 'альбомы'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['album', 'order', '-upload_at'], 'verbose_name': 'фотография', 'verbose_name_plural': 'фотографии'},
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='album',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='изменено'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album', verbose_name='альбом'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='order',
            field=models.IntegerField(default=0, verbose_name='порядок'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=albums.models.get_upload_path, verbose_name='файл'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='добавлено'),
        ),
        migrations.AlterUniqueTogether(
            name='photo',
            unique_together={('album', 'order')},
        ),
    ]