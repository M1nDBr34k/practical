from django.contrib import admin
from .models import Car, Rental, AddOn, Location, Review

admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(AddOn)
admin.site.register(Location)
admin.site.register(Review)
# Register your models here.
