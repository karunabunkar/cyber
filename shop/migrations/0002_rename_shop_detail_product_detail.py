# Generated by Django 3.2.7 on 2022-01-17 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shop_detail',
            new_name='product_detail',
        ),
    ]
