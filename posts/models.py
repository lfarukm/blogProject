from django.db import models

import uuid
from user.models import *
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, related_name='Owners' ,on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = RichTextField(max_length=500, verbose_name='İçerik')
    image = models.FileField(upload_to='posts/', verbose_name='Thumbnail')
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(Profile, related_name='likes' , verbose_name='Beğenenler', blank=True)
    dislike = models.ManyToManyField(Profile, related_name='dislikes' , verbose_name='Beğenmeyenler', blank=True)
    isPublish = models.BooleanField(default=False, verbose_name='Yayınla')

    slug = models.SlugField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı','i'))
        super().save(*args, **kwargs)
        





