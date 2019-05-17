from django.contrib import admin
#adminname: admin
#psw: weiyubing
# Register your models here.
from .models import Custom,LedNumber,Picture,Video

@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
	list_display =('id','user_name','user_password')
	ordering =('id',)

@admin.register(LedNumber)
class LedNumberAdmin(admin.ModelAdmin):
	list_display = ('id','custom','led_text','address_text')
	ordering = ('id',)

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
	list_display = ('id','custom','pic_url')
	ordering = ('id',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ('id','custom','video_url')
	ordering = ('id',)

