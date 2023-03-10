# Generated by Django 4.1.2 on 2023-01-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_question_profile_address_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='eth_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='private_key',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='xml_balance',
            field=models.FloatField(default=0),
        ),
    ]
