from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms to display


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'carmake', 'cartype', 'year']
    list_filter = ['carmake', 'cartype', 'year']
    search_fields = ['name', 'carmake__name', 'cartype']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
