from django.contrib import admin
from .models import Animal, Type, Genus
# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','available')
    list_filter = ('available',)
    search_fields = ('name','description')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}     

@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}         