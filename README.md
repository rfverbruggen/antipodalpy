Antipodalpy
===========
A python library to calculate the Antipodal point of a location on a sphere. E.g. the earth.

Always wanted to know where you would end up if you dug a hole to the other side of the earth?

In mathematics, the antipodal point of a point on the surface of a sphere is the point which is diametrically opposite to it — so situated that a line drawn from the one to the other passes through the center of the sphere and forms a true diameter.

Usage
-----
```python
from antipodalpy import Antipodal, Location

location = Location(19.568469, 204.19083341) # lat, lon

antipodal = Antipodal(location)
print antipodal.lat # -19.568469
print antipodal.lon # -24.19083341
```