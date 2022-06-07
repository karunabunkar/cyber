# Generated by Django 3.2.6 on 2022-03-07 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('img', models.ImageField(upload_to='img/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('about', models.TextField()),
                ('address', models.TextField(default='India')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_record', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]