from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name_project', 'description', 'coordinate', 'latitude', 'longitude', 'altitudealti', 'point_x', 'point_y', 'point_z', 'altitudes_elavation', 'accountable', 'status', 'slug','image']