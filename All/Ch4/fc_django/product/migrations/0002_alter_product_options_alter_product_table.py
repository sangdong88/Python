# Generated by Django 4.0 on 2022-01-04 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '상품', 'verbose_name_plural': '상품'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='fastcampus_product',
        ),
    ]
