from django.db import models

from django.contrib.auth.models import User
import uuid #? burdaki import ise bize rastgale id oluşturuyor.
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False) #* burdaki primary_key ise bu idyi başkası kullanamaz diye tanımlıyoruz. 'editable' bu ise kullanıcı bunu değiştiremez diye tanımlıyoruz.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='İsim') #* burdaki 'verbose_name' veri tabanındaki o başlığı düzenliyoruz.
    surname = models.CharField(max_length=100, verbose_name='Soyisim')
    bio = models.TextField(max_length=500, verbose_name='hakkımda' , default='Merhaba Ben Bir Blog Yazarıyım.')
    image = models.FileField(upload_to='profiles/', null=True , verbose_name='Profil Resmi', default='profiles/defaultt pp.jpeg') #* burdaki default ise otomatikmen resim ekliyoruz aynı şekilde yukardaki biodada aynı şekilde oluyor.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulduğu Tarih')
    follow = models.ManyToManyField('self', symmetrical=False,related_name='takip',verbose_name='Takip', blank=True)
    followers = models.ManyToManyField('self',symmetrical=False, related_name='takipçi', verbose_name='Takipçi', blank= True)

    slug = models.SlugField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username.replace('ı','i'))
        super().save(*args, **kwargs)