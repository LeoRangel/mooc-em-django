from django.contrib import admin

from .models import Course

# Customizar vizualização do model no admin
class CourseAdmin(admin.ModelAdmin):
    # O que mostra
    list_display = ['name', 'slug', 'start_date', 'created_at']
    # Pesquisar nestes campos
    search_fields = ['name', 'slug']
    # Preencher campo automaticamente
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Course, CourseAdmin)