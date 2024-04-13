from django.contrib import admin
from .models import Singer


# Register your models here.
class SingerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Singer, SingerAdmin)
