# We acknowledge the use of imagery provided by services from NASA's Global Imagery Browse Services (GIBS), part of NASA's Earth Science Data and Information System (ESDIS).

from owslib.wms import WebMapService
from datetime import date

# Connect to NASA GIBS WMS endpoint
wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

coordinates = (38.0326706910698, -84.50367246570195) # lat, lon
dt = .1
box = (
    coordinates[1] - dt,
    coordinates[0] - dt,
    coordinates[1] + dt,
    coordinates[0] + dt
)

# Request map image
img = wms.getmap(
    layers=['MODIS_Terra_CorrectedReflectance_TrueColor'],
    srs='EPSG:4326',
    bbox=box,
    size=(4096, 4096),
    format='image/png',
    transparent=False,
    time=date.today()
)

# Save image to file
with open('map.png', 'wb') as f:
    f.write(img.read())