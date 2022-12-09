from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notice, NoticeAdmin)
