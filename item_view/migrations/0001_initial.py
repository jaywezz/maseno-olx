# Generated by Django 2.2.5 on 2019-10-14 10:01

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField(max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_image', models.ImageField(upload_to='items')),
                ('item_category', models.CharField(choices=[('Select category', 'Select Category'), ('Laptops', 'Laptops'), ('Phones', 'Phones'), ('House equipments', 'House equipments'), ('Electronics', 'Electronics'), ('Clothes', 'Clothes'), ('Shoes', 'Shoes'), ('Stationary', 'Stationary')], default=0, max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('item_owner', models.ForeignKey(default=authentication.models.DaemonStar_User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]