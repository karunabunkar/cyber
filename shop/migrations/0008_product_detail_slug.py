# Generated by Django 3.2.7 on 2022-01-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detail',
            name='slug',
            field=models.SlugField(max_length=1000, null=True),
        ),
    ]