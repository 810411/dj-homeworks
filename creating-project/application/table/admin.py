from django.contrib import admin

from .models import TableField, PathToCsv
# Register your models here.


admin.site.register(TableField)

admin.site.register(PathToCsv)
