# Generated by Django 3.2.7 on 2022-02-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_course_detail_dec'),
    ]

    operations = [
        migrations.AddField(
            model_name='crs_review',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]