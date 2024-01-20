from django.contrib import admin
from .models import Section,Student
# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=['id','name','section']