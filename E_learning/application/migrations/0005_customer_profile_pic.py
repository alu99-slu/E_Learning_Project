# Generated by Django 3.2.5 on 2021-08-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_course_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
