# Generated by Django 3.2.7 on 2022-01-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crs_img', models.ImageField(upload_to='')),
                ('usr_img', models.ImageField(upload_to='')),
                ('crs_title', models.CharField(max_length=1000)),
                ('usr_name', models.CharField(max_length=100)),
                ('crs_descrption', models.TextField()),
                ('lession_no', models.IntegerField()),
                ('std_no', models.IntegerField()),
                ('crs_price', models.IntegerField(default='Free')),
            ],
        ),
    ]