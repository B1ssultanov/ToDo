from django.contrib import admin

from main.models import List, Complete, Users


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


@admin.register(Complete)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

@admin.register(Users)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone')
