# Generated by Django 3.2.4 on 2021-06-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztp5', '0008_alter_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishmodel',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
