# Generated by Django 3.2.4 on 2021-06-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210607_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(default=0, upload_to='media'),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='img',
            field=models.ImageField(default=0, upload_to='media'),
        ),
        migrations.AddField(
            model_name='postmediacategory',
            name='img',
            field=models.ImageField(default=0, upload_to='media'),
        ),
    ]
