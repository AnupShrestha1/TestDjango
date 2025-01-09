# Generated by Django 5.1.4 on 2025-01-08 22:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_options_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]