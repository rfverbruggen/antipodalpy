class Location(object):
	"""docstring for Location"""
	def __init__(self, lat=0, lon=0):
		self._lat = lat
		self._lon = lon

	def __str__(self):
		return "Location(%s,%s)" % (self._lat, self._lon)

	def __unicode__(self):
		return u"Location(%s,%s)" % (self._lat, self._lon)

	@property
	def lat(self):
		return self._lat
	@lat.setter
	def lat(self, value):
		self._lat = value

	@property
	def lon(self):
		return self._lon
	@lon.setter
	def lon(self, value):
		self._lon = value

class Antipodal(Location):
	"""docstring for Antipodal"""
	def __init__(self, lat, lon):
		Location.__init__(self, 0, 0)
		self.calcLat(lat)
		self.calcLon(lon)

	def calcLat(self, lat):
		self._lat = -lat

	def calcLon(self, lon):
		self._lon = 180-lon