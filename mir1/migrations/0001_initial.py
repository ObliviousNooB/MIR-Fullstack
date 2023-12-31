# Generated by Django 4.1.5 on 2023-01-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('userid', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('userstate', models.CharField(choices=[('1', 'Andhra Pradesh'), ('2', 'Arunachal Pradesh'), ('3', 'Assam'), ('4', 'Bihar'), ('5', 'Chhattisgarh'), ('6', 'Goa'), ('7', 'Gujarat'), ('8', 'Haryana'), ('9', 'Himachal Pradesh'), ('10', 'Jharkhand'), ('11', 'Karnataka'), ('12', 'Kerala'), ('13', 'Madhya Pradesh'), ('14', 'Maharashtra'), ('15', 'Manipur'), ('16', 'Meghalaya'), ('17', 'Mizoram'), ('18', 'Nagaland'), ('19', 'Odisha'), ('20', 'Punjab'), ('21', 'Rajasthan'), ('22', 'Sikkim'), ('23', 'Tamil Nadu'), ('24', 'Telangana'), ('25', 'Tripura'), ('26', 'Uttarakhand'), ('27', 'Uttar Pradesh'), ('28', 'West\xa0Bengal')], max_length=30)),
                ('usertype', models.CharField(max_length=10)),
                ('viewlevel', models.IntegerField(max_length=1)),
            ],
        ),
    ]
