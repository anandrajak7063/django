from django.contrib import admin
from .models import *

# Register your models here.
class hoteladmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price','hotel_description']


admin.site.register(amenities)
admin.site.register(hotel,hoteladmin)
admin.site.register(hotelImage)
