from django.contrib import admin
from .models import MusicLibrary


# Register your models here.
class MusicLibraryAdmin(admin.ModelAdmin):
    pass


admin.site.register(MusicLibrary, MusicLibraryAdmin)
