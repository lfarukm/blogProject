# Generated by Django 4.1.7 on 2023-03-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_dislike_alter_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]