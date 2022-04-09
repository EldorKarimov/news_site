from django.contrib import admin
from .models import Category, City, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

@admin.register(City)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

@admin.register(News)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'views', 'tags']
    prepopulated_fields = {"slug":['title']}