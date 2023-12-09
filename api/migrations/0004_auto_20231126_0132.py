# Generated by Django 3.2 on 2023-11-26 06:32

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]
