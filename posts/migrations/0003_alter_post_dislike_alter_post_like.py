# Generated by Django 4.1.7 on 2023-03-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_image_alter_profile_bio'),
        ('posts', '0002_post_ispublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to='user.profile', verbose_name='Beğenmeyenler'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to='user.profile', verbose_name='Beğenenler'),
        ),
    ]