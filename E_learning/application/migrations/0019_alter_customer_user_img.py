# Generated by Django 3.2.5 on 2021-08-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_alter_customer_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_img',
            field=models.ImageField(default='profile1.png', upload_to='user_images'),
        ),
    ]
