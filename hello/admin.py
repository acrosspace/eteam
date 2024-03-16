from django.contrib import admin

# Register your models here.

from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
    #list_display = ('name', 'description', 'created_date', 'contact_email', 'is_active')
    #list_filter = ['created_date']
    #search_fields = ['name', 'description']