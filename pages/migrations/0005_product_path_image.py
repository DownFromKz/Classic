# Generated by Django 4.0.4 on 2022-05-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='path_image',
            field=models.TextField(default='', verbose_name='Путь к файлу с изображением'),
            preserve_default=False,
        ),
    ]