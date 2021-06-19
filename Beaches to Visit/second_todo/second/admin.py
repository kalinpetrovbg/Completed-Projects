from django.contrib import admin
from second_todo.second.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'distance']
