from django.contrib import admin
from .models import *

class koordinatadmin(admin.ModelAdmin):
    list_display = ['nama_penyu', 'alamat', 'koordinat']
    search_fields = ['alamat']
    list_per_page = 5

class klasifikasiadmin(admin.ModelAdmin):
    list_display = ['nama_ilmiah', 'nama_lokal', 'spesies']
    search_fields = ['nama_ilmiah']
    list_per_page = 5



admin.site.register(Koordinat, koordinatadmin)
admin.site.register(Klasifikasi, klasifikasiadmin)


# Register your models here.
