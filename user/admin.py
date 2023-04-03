from django.contrib import admin

from .models import *

#? burda veri tabanımızda görünmesini istediğmiz şeyleri yaziyoruz.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'created_at', 'id') #* burda hangi bilgilerin görünmesini istediğmizi seçip yaziyoruz.
    list_display_links = ('user', 'name') #* hangisinin tıklanmasını gösteriyoruz.
    search_fields = ('name',) #* burda ise bize arama çubuğu gösteriyor. tek bir değer girsek bile sonuna virgül koymayı unutma.
    date_hierarchy = 'created_at' #* tarihe göre filtreleme yapar.
    list_filter = ('user', 'surname') #* burda ise neye göre filtereleme yapmamızı sağlıyor.
    # list_editable = ('surname',) #* burda değştirmek istediğmizi şeyleri yaziyoruz. sonuna tek değer girsekte virgül koy.
    list_per_page = 15 #* burda 1 sayfada kaç tane içerik gösterildiğni yaziyoruz.
    readonly_fields = ('id', 'created_at', 'slug') #* burda ise değiştiremiyoruz ama bilgilerin içinde gözükmesini istiyorsak kullanabilir.
    

# Register your models here.
admin.site.register(Profile, ProfileAdmin)

