from django.contrib import admin
from .models import Entyre

class EntyreAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'dob', 'age', 'weight', 'insurance_comp', 'insurance_num')

# Register your models here.

admin.site.register(Entyre, EntyreAdmin)
