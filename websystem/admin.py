from django.contrib import admin

# Register your models here.
from .models import Channel1_data
from .models import Channel2_data
from .models import Channel3_data

# Django管理サイトにWebsystemを登録する


class Channel1Admin(admin.ModelAdmin):
    list_display = ("id","content")

    list_display_links = ("id","content")

class Channel2Admin(admin.ModelAdmin):
    list_display = ("id","content")

    list_display_links = ("id","content")

class Channel3Admin(admin.ModelAdmin):
    list_display = ("id","content")

    list_display_links = ("id","content")


admin.site.register(Channel1_data)
admin.site.register(Channel2_data)
admin.site.register(Channel3_data)