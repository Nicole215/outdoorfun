# Generated by Django 4.2.17 on 2025-01-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoorevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisator',
            name='contact_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisator',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
