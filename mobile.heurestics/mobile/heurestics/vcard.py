"""

    vCard download generation

    vObject Python package needed: http://vobject.skyhouseconsulting.com/'
    
"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 Twinapex Research"
__license__ = "GPL"
__docformat__ = "epytext"


from StringIO import StringIO

from mobile.sniffer.utilities import get_user_agent

from mobile.heurestics.simple import is_apple_device, is_blackberry, is_android  

import vobject
from vobject import vcard
from vobject import base

class TelBehavior(vcard.VCardBehavior):
    """ A quick hack to implement Tel behavior (missing from vobject lib) """
    hasNative = True


base.registerBehavior(TelBehavior, 'TEL')


def create_vcard(first_name=None, 
                 last_name=None,
                 title=None, 
                 company=None, 
                 email=None, 
                 street=None, 
                 region=None,
                 country=None, 
                 city=None, 
                 postal_code=None, 
                 landline_number=None,
                 mobile_number=None,
                 latitude=None,
                 longitude=None,
                 www_link=None,
                 www_link_2=None):
    """ Create a vCard payload.
    
    Create payload for vCard transfered via SMS, email or HTTP download.
    
    TODO: handle encoding internally - currently pre-encoded strings assumed
    
    TODO: Support geolocation extensions
 
    vCard specification: 
        
        * http://www.ietf.org/rfc/rfc2426.txt
        
    More info:
    
        * http://vobject.skyhouseconsulting.com/usage.html
        
        * http://svn.osafoundation.org/vobject/trunk/vobject/vcard.py
        
        * http://en.wikipedia.org/wiki/VCard

        
    @return: 8-bit string, using input encoding. 
    """
    
    j = vobject.vCard()
    
    if first_name and last_name:
        j.add('n')
        j.n.value = vobject.vcard.Name(family=last_name, given=first_name)        
        j.add('fn')
        j.fn.value = first_name + " " + last_name
    else:
        # vCard limitation - must be at least one fn element
        raise RuntimeError("First name and last name must be given")
    if title:
        j.add('title')
        j.title.value = title
    if email:
        j.add('email')
        j.email.value = email
        j.email.type_param = 'INTERNET'
        
    if street or region or country or city or postal_code:
        j.add("adr")
        j.adr.value = vcard.Address()
        adr = j.adr.value
        if street:
            adr.street = street
        if region:
            adr.region = region
        if postal_code:
            adr.code = postal_code
        if city:
            adr.city = city
        if country: 
            adr.country = country
        
    if company:
        j.add("org")
        j.org.value = [company]
        
    
    if landline_number:
        tel = j.add("tel")        
        tel.type_param = ["WORK","VOICE"]
        tel.value = landline_number

    if mobile_number:
        tel = j.add("tel")        
        tel.type_param = ["WORK","MOBILE"]
        tel.value = mobile_number
                
    if www_link:
        url = j.add("url")
        url.value = www_link

    if www_link_2:
        url = j.add("url")
        url.value = www_link_2
          
    if latitude and longitude:
        # Not supported yet
        pass
            
    return j.serialize()

    
def is_vcard_supported(request):
    """
    @return: True if the device which made HTTP request can support HTTP downloadable vCards
    """
    if is_apple_device(request) or is_blackberry(request) or is_android(request):
        return False
    
    return True
    