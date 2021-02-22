# Generated by Django 3.1.4 on 2021-02-22 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0014_auto_20210222_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
