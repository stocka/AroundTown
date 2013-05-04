from django.http import HttpResponse
from django.utils import simplejson, formats
from django.shortcuts import render
from aroundtown import mapsettings
from locations.models import Location

def index(request):
	locations = Location.objects.all()
	context = {'map_settings': mapsettings.MapSettings(), 'locations': locations}
	return render(request, 'index.html', context)

def detail(request, location_id):
	try:
		location = Location.objects.get(pk=location_id)
		visits = location.visit_set.all().order_by('visit_date')

		to_json = {
	    "name": location.name,
	    "address": location.formatted_address,
	    "visits": []
		}

		if location.last_visited_date:
			to_json["last_visited"] = formats.date_format(location.last_visited_date, "SHORT_DATETIME_FORMAT")

		for visit in visits:
			to_json['visits'].append({
				"date": formats.date_format(visit.visit_date, "SHORT_DATETIME_FORMAT"),
				"rating": str(visit.rating) + ' - ' + str(visit.RATINGS[visit.rating][1]),
				"writeup": visit.writeup
			})

		return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')	
	except Location.DoesNotExist:
		raise Http404