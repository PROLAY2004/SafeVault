# Generated by Django 5.1.5 on 2025-02-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
