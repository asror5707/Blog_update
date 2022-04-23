from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Maqola,Rasm,Comment,About
@admin.register(Maqola)
class MaqolaAdmin(ModelAdmin):
    search_fields = ['id','title','matn','time']
    list_display = ['title','matn','time']

@admin.register(About)
class AboutAdmin(ModelAdmin):
    search_fields = ['id','matn','rasm']
    list_display = ['matn','rasm']
admin.site.register(Rasm)
admin.site.register(Comment)
# Register your models here.
