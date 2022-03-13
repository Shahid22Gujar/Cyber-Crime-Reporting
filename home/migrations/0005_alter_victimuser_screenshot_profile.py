# Generated by Django 4.0.3 on 2022-03-13 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_victimuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victimuser',
            name='screenshot',
            field=models.ImageField(upload_to='screenshot/'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_img')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
