# Generated by Django 2.2.6 on 2019-10-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20191016_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daemonstar_user',
            name='user_avatar',
            field=models.ImageField(blank=True, default='/profiles/3.jpg', upload_to='profiles'),
        ),
    ]