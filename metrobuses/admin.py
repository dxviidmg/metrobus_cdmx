from django.contrib import admin
from metrobuses.models import Metrobus



class MetrobusAdmin(admin.ModelAdmin):
    ordering = ['metrobus_id']
    search_fields = ['metrobus_id']
#    list_display = ('alcaldia')
#    list_filter = ('alcaldia')

admin.site.register(Metrobus, MetrobusAdmin)