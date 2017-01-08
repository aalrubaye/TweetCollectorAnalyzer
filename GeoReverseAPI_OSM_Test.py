__author__ = 'Abduljaleel'

import geopy
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim()

try:
    # tweet['geo_coordinates']
    a = [-73.757872, 33.384994]
    geoloc = geolocator.reverse(str(a[1])+','+str(a[0]))
    print geoloc.address


    # loc = 'enter your' tweet['user']['location']
    geoloc = geolocator.geocode(loc)
    print geoloc.address


    time.sleep(0.5)
except Exception as ex:
    print 'ERROR3:',ex