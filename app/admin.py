from django.contrib import admin
from .models import *
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']
    list_per_page = 10

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','book']
    list_per_page = 10

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)