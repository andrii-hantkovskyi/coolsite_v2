from django.contrib import admin
# Register your models here.
from django.contrib.admin import ModelAdmin

from main.models import GameCategory, Game, Post


@admin.register(GameCategory)
class GameCategoryAdmin(ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id',)
    list_editable = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Game)
class GameAdmin(ModelAdmin):
    fields = ('category', 'slug', 'name', 'description', 'image', 'pub_date')
    list_display = ('id', 'category', 'name', 'pub_date')
    list_display_links = ('id',)
    list_editable = ('name',)
    list_filter = ('category',)
    ordering = ('pub_date',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(ModelAdmin):
    fields = ('game', 'title', 'content', 'pub_date', 'last_update', 'in_archive')
    list_display = ('id', 'title', 'pub_date', 'last_update', 'in_archive')
    list_editable = ('title', 'in_archive')
    readonly_fields = ('pub_date', 'last_update')
    list_display_links = ('id',)
    search_fields = ('title',)
