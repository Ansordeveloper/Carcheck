from django.contrib import admin

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership, CarPost

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color', 'year', 'rudder_location', 'engine_volume']
    list_filter = ['license_plate', 'brand', 'model', 'color', 'year', 'rudder_location', 'engine_volume'] 
    list_per_page = 20
    search_fields = ['license_plate', 'brand', 'model', 'color', 'year', 'rudder_location', 'engine_volume']

@admin.register(SpecialMarks)
class SpecialMarksAdmin(admin.ModelAdmin):
    list_display = ['car','title']
    list_filter = ['car', 'title']
    list_per_page = 20
    search_fields = ['car__brand','title']


@admin.register(PeriodsOwnership)
class PeriodsOwnershipAdmin(admin.ModelAdmin):
    list_display = ['car','from_date','before_date','actual']
    list_filter = ['car','from_date','before_date','actual']
    list_per_page = 20
    search_fields = ['car__brand','from_date','before_date','actual']

@admin.register(CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'price']
    list_filter = ['brand', 'model', 'price']
    list_per_page = 20
    search_fields = ['brand', 'model', 'price']