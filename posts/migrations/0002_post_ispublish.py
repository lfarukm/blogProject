# Generated by Django 4.1.7 on 2023-03-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isPublish',
            field=models.BooleanField(default=False, verbose_name='Yayınla'),
        ),
    ]
