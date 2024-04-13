from django.contrib import admin
from .models import Player


# Register your models here.
class playerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, playerAdmin)
