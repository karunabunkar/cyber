# Generated by Django 3.2.6 on 2022-02-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_page_info_about_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_page_info',
            name='about_contact',
            field=models.TextField(blank=True, null=True),
        ),
    ]