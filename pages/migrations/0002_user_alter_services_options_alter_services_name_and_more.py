# Generated by Django 4.0.4 on 2022-05-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15, verbose_name='Псевдоним')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('password', models.CharField(max_length=15)),
                ('is_employee', models.BooleanField(verbose_name='Сотрудник')),
            ],
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'услугу', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
    ]
