# Generated by Django 3.2.4 on 2021-06-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztp5', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
