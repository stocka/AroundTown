from django.contrib import admin
from locations.models import Location, Visit

class LocationAdmin(admin.ModelAdmin):
	list_display = ['name', 'formatted_address', 'last_visited_date']

class VisitAdmin(admin.ModelAdmin):
	list_display = ['visit_date', 'rating']
	list_filter = ['location', 'visit_date', 'rating']

admin.site.register(Location, LocationAdmin)
admin.site.register(Visit, VisitAdmin)
