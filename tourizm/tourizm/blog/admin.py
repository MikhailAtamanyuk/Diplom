from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'cat')
    list_display_links = ('title', 'cat')
    search_fields = ('title', 'cat')
    list_filter = ('cat',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


admin.site.register(City, BlogAdmin)
admin.site.register(Country, CategoryAdmin)

