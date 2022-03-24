# Generated by Django 4.0.3 on 2022-03-24 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_rename_victimuser_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='crime_source',
        ),
        migrations.RemoveField(
            model_name='report',
            name='id_usedby_criminal',
        ),
        migrations.RemoveField(
            model_name='report',
            name='suspected_person',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user_adhar',
        ),
        migrations.AddField(
            model_name='report',
            name='additional_information',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='incident_place',
            field=models.CharField(default='Delhi', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='reason_for_reporting',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='mobile',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='report',
            name='suspected_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]