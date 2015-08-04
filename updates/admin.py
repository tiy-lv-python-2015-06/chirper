from django.contrib import admin
from updates.models import Chirp


@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'posted_at']
