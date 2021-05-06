from django.contrib import admin
from .models import Medicine

class MedicineInfo(admin.ModelAdmin):
    list_display = ('id', 'name', 'ingredient', 'effect', 'dosage')

admin.site.register(Medicine, MedicineInfo)