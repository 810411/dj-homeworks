from django.contrib import admin
from .models import Manufacturer, Phone


# Register your models here.

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass
