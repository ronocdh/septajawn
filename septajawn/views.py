# Create your views here.
from django.http import HttpResponse
import septapy.route

import json
import requests


def getNearestStop(request, route=None, lat=None, lng=None):

    r = septapy.route.Route(route)

    # form data comes in as unicode via GET, so convert to float
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    #print "LAT LONG ARE: %s %s" % (lat, lng)

    n = r.nearestStop(lat, lng)
    d = dict(title=n.title, lat=n.latitude, lng=n.longitude)
    j = json.dumps(d)

    return HttpResponse(j, mimetype='application/json')

def getNearestTrolley(request, route=None, lat=None, lng=None):

    r = septapy.route.Route(route)

    # form data comes in as unicode via GET, so convert to float
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))

    n = r.nearestVehicle(lat, lng)

    # poor man's object serialization right here. 
    d = dict(direction=n.direction, title=n.title, lat=n.latitude, lng=n.longitude)
    j = json.dumps(d)

    return HttpResponse(j, mimetype='application/json')
