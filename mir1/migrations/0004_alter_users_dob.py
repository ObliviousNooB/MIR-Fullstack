# Generated by Django 4.1.5 on 2023-01-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir1', '0003_users_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateField(default='2023.01.01'),
        ),
    ]