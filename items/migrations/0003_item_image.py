# Generated by Django 3.1.4 on 2020-12-12 06:46

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201212_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=items.models.item_directory_path),
        ),
    ]
