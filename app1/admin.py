from django.contrib import admin
from app1 import models

# Register your models here.
@admin.register(models.Student)
class listview(admin.ModelAdmin):
    list_display=['id','name','age','address','Subject']
# admin.site.register(models.Student,listview)
