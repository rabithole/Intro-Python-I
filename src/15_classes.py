# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
	def __init__(self, name, lat, lon ):
		self.name = name
		self.lat = lat
		self.lon = lon

x = LatLon('Lost', 9, 19)
print(x.lat, x.lon, x.name)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
	def __init__(self, name, lat, lon):
		super().__init__(name, lat, lon)

y = Waypoint('Home', 134, 23)
print(f'{y.name}: {y.lat}, {y.lon}')
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(LatLon):
	def __init__(self, name, lat, lon, difficulty, size):
		super().__init__(name, lat, lon)
		self.difficulty = difficulty
		self.size = size
	def __str__(self):
		return f'{self.name}: {self.difficulty}, {self.size}, {self.lat}, {self.lon}'

z = Geocache('Park', 45, 33, 2, 3)
print(f'Line 36: {z.name}, {z.lat}, {z.lon}, {z.difficulty}')
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
Waypoint = Geocache('Catacombs', 41.70505, -121.51521, 4, 2)
print(Waypoint.name, Waypoint.lat, Waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
# print(Newberry)
