# call with 2 arguments: longitude, latitude

from staticmap import StaticMap, CircleMarker
import sys

size = 600
m = StaticMap(size, size)
m.add_marker(CircleMarker((float(sys.argv[1]), float(sys.argv[2])), 'blue', 8)) # add marker in center
image = m.render(zoom=15) # make image
image.save("map.png")