# Generated by Django 2.2.6 on 2019-10-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_view', '0003_auto_20191031_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]
