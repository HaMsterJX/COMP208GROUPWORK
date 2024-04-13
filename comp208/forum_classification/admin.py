from django.contrib import admin
from .models import ForumClassification


# Register your models here.
class ForumClassficationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ForumClassification, ForumClassficationAdmin)

