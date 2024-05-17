from django.contrib import admin

from space.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria","legenda", "publicada", "data_fotografia")
    list_display_links = ("id", "nome",)
    list_filter = ("categoria",)
    search_fields = ("id", "nome")
    list_editable = ("publicada",)
    list_per_page = 10
    ordering = ("id",)
    
    
admin.site.register(Fotografia, ListandoFotografias)
