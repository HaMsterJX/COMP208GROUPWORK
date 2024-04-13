from django.contrib import admin
from .models import forum


# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    pass


admin.site.register(forum, ForumAdmin)

