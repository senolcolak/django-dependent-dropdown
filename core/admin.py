from django.contrib import admin
from .models import City,Country,District,Event

# Register your models here.


admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Event)