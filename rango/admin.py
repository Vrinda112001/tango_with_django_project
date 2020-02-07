from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    #def __init__(self):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
