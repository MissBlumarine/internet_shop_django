from django.contrib import admin

from .models import Boardgame


@admin.register(Boardgame)
class BoardgameAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "issue_year", "price"
    list_display_links = "name", "pk"
    ordering = "pk",
