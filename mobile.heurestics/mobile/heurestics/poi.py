"""

    Point-of-interest generation


"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 Twinapex Research"
__license__ = "GPL v2" 
__docformat__ = "epytext"


from StringIO import StringIO

from mobile.sniffer.utilities import get_user_agent

def nokia_poi(name=None, lng=None, lat=None, link=None, street=None,
              country=None, city=None, postal_code=None, phone_number=None, media_name=None):
    """
    Create Nokia Landmarks API compatible download.

    You need to set response content type to application/vnd.nokia.landmarkcollection+xml; charset=utf-8
    """
    buf = StringIO()
    print >> buf, """<?xml version="1.0" encoding="UTF-8"?>"""
    print >> buf, """<lm:lmx xmlns:lm="http://www.nokia.com/schemas/location/landmarks/1/0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.nokia.com/schemas/location/landmarks/1/0/ lmx.xsd">"""
    print >> buf, "<lm:landmark>"

    if name:
        print >> buf, "<lm:name>%s</lm:name>" % name

    if lng != None:
        print >> buf, "<lm:coordinates>"
        print >> buf, "  <lm:latitude>%s</lm:latitude>" % lat
        print >> buf, "  <lm:longitude>%s</lm:longitude>" % lng
        print >> buf, "</lm:coordinates>"

    if street or country or city or postal_code or phone_number:
        print >> buf, "<lm:addressInfo>"
        if country:
            print >> buf, "<lm:country>%s</lm:country>" % country

        if city:
            print >> buf, "<lm:city>%s</lm:city>" % city

        if postal_code:
            print >> buf, "<lm:postalCode>%s</lm:postalCode>" % postal_code

        if street:
            print >> buf, "<lm:street>%s</lm:street>" % street

        if phone_number:
            print >> buf, "<lm:phoneNumber>%s</lm:phoneNumber>" % phone_number
        
        print >> buf, "</lm:addressInfo>"

    if link:
        print >> buf, "<lm:mediaLink>"
        print >> buf, "<lm:url>%s</lm:url>" % link
        print >> buf, "</lm:mediaLink>"
        print >> buf, "<lm:category>"
        print >> buf, "<lm:id>10000</lm:id>"
        
        if media_name:
            print >> buf, "<lm:name>%s</lm:name>" % media_name
        
        print >> buf, "</lm:category>"

    print >> buf, "</lm:landmark>"
    print >> buf, "</lm:lmx>"

    return buf.getvalue()

def get_google_maps_link(lat, lng, zoom=13, type="m"):
    """
    http://www.alistapart.com/articles/putyourcontentinmypocket/

    http://mapki.com/wiki/Google_Map_Parameters
    """

    return "http://maps.google.com/maps/?q=%f,%f&z=%d&t=%s" % (lat, lng, zoom, type)


def get_poi_type(request):
    ua = get_user_agent(request)
    if ua:
        ua = ua.lower()
        if "nokia" in ua:
            return "landmark"
        elif "iphone" in ua:
            return "href"
