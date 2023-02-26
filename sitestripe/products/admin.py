from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_display_links = ("id", "name", "price")
    search_fields = ("name", "description")


admin.site.register(Item, ItemAdmin)
