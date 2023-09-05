from django.contrib import admin

from main.models import List, Complete


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


@admin.register(Complete)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
