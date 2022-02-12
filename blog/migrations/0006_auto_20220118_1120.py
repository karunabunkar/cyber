# Generated by Django 3.2.7 on 2022-01-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220118_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_detail',
            name='element',
        ),
        migrations.AddField(
            model_name='blog_detail',
            name='element',
            field=models.ManyToManyField(null=True, related_name='blog_element', to='blog.blogdetail_element'),
        ),
        migrations.RemoveField(
            model_name='blog_detail',
            name='imgs',
        ),
        migrations.AddField(
            model_name='blog_detail',
            name='imgs',
            field=models.ManyToManyField(null=True, related_name='blog_img', to='blog.blogdetail_img'),
        ),
    ]