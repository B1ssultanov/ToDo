# Generated by Django 4.2.1 on 2023-09-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_list_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=1, max_length=100, verbose_name='password'),
            preserve_default=False,
        ),
    ]
