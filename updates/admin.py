from django.contrib import admin
from updates.models import Chirp, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'posted_at']
