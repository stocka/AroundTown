from aroundtown import settings
from aroundtown import local_settings

class MapSettings:

	def __init__(self):

		try:
			self.zoom = local_settings.DEFAULT_MAP_ZOOM
		except Exception, e:
			self.zoom = settings.DEFAULT_MAP_ZOOM
		else:
			pass

		try:
			self.latitude = local_settings.DEFAULT_MAP_LATITUDE
		except Exception, e:
			self.latitude = settings.DEFAULT_MAP_LATITUDE
		else:
			pass

		try:
			self.longitude = local_settings.DEFAULT_MAP_LONGITUDE
		except Exception, e:
			self.longitude = settings.DEFAULT_MAP_LONGITUDE
		else:
			pass						
		
		self.key = local_settings.GOOGLE_MAPS_API_KEY
