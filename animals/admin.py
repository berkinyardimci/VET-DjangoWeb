from django.contrib import admin
from .models import Animal
# Register your models here.

@admin.register(Animal)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','available')
    list_filter = ('available',)
    search_fields = ('name','description')
