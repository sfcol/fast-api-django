from django.contrib import admin

from api.models import Item , User


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(User)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")