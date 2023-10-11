from django.contrib import admin
from user.models import Vevar
# Register your models here.

class VevarAdmin(admin.ModelAdmin):
    list_display=('name','village','vevar','date')
    search_fields=('name','village')
    
admin.site.register(Vevar, VevarAdmin)