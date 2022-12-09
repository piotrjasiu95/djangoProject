# Generated by Django 3.2.4 on 2021-06-21 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ztp5', '0005_remove_dishmodel_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('adres_1', models.CharField(blank=True, max_length=30, null=True)),
                ('adres_2', models.CharField(blank=True, max_length=30, null=True)),
                ('dish', models.ManyToManyField(to='ztp5.DishModel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
