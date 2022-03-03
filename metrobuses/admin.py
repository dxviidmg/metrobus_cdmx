from django.contrib import admin
from metrobuses.models import Metrobus



class MetrobusAdmin(admin.ModelAdmin):
    ordering = ['number']
    search_fields = ['number']


admin.site.register(Metrobus, MetrobusAdmin)