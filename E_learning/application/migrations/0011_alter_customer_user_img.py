# Generated by Django 3.2.5 on 2021-08-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20210809_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_img',
            field=models.ImageField(default='profile1.png', upload_to='user_images'),
        ),
    ]