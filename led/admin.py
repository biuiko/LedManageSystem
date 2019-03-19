from django.contrib import admin
#adminname: admin
#psw: weiyubing
# Register your models here.
from .models import Custom

admin.site.register(Custom)