# Generated by Django 4.2.1 on 2023-09-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.users'),
            preserve_default=False,
        ),
    ]