# Generated by Django 5.1.6 on 2025-02-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0014_userdata_unique_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='unique_key',
            field=models.CharField(default=0, max_length=6, unique=True),
        ),
    ]
