from django.contrib import admin

from .models import Boardgame, BoardgameAge, Addition

@admin.register(Boardgame)
class BoardgameAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "issue_year", "price"
    list_display_links = "name", "pk"
    ordering = "pk",


@admin.register(BoardgameAge)
class BoardgameAgeAdmin(admin.ModelAdmin):
    list_display = "pk", "age",
    list_display_links = "age",


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "issue_year", "price"
    list_display_links = "name", "pk"
    ordering = "pk",