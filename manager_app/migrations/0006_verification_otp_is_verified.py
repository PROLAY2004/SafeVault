# Generated by Django 5.1.5 on 2025-02-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0005_alter_verification_otp_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification_otp',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
