from django.contrib import admin
from .models import Banda, Album, Musica

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'lancamento')
    list_filter = ('banda', 'lancamento')
    search_fields = ('titulo',)

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao', 'link_spotify')
    list_filter = ('album',)
    search_fields = ('titulo',)

admin.site.register(Banda)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
