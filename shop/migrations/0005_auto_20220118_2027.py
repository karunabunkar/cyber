# Generated by Django 3.2.7 on 2022-01-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_order',
            name='phone',
            field=models.IntegerField(),
        ),
    ]