# Generated by Django 3.0.7 on 2020-07-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200716_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexblog',
            name='text2',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Text2'),
        ),
        migrations.AddField(
            model_name='indexblog',
            name='title2',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Title2'),
        ),
    ]
