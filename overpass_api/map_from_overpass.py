# call with 2 arguments: latitude, longitude
# use negative numbers for south or west
# program will exit with 0 if the map was generated successfully
# program will exit with 1 if the map could not be generated, likely you are not connected to the internet

from staticmap import StaticMap, CircleMarker
import sys

size = 600
try:
    m = StaticMap(size, size)
    m.add_marker(CircleMarker((float(sys.argv[2]), float(sys.argv[1])), 'blue', 8)) # add marker in center
    image = m.render(zoom=13) # make image
    image.save("map.png")
    sys.exit(0)
except Exception:
    sys.exit(1)