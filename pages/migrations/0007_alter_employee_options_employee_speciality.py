# Generated by Django 4.0.4 on 2022-05-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_employee_delete_user_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'сотрудников', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='employee',
            name='speciality',
            field=models.CharField(default='сотрудник', max_length=150),
            preserve_default=False,
        ),
    ]
