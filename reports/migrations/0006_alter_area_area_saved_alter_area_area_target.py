# Generated by Django 4.1.5 on 2023-01-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_alter_state_achieved_alter_state_cum_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_saved',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='area',
            name='area_target',
            field=models.CharField(max_length=7),
        ),
    ]