# Generated by Django 4.2.1 on 2023-09-07 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_complete_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthday',
        ),
    ]
