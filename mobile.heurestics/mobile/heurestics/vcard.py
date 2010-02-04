"""

    vCard download generation

    vObject dependency needed: http://vobject.skyhouseconsulting.com/
"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 Twinapex Research"
__license__ = "GPL"
__docformat__ = "epytext"


from StringIO import StringIO

from mobile.sniffer.utilities import get_user_agent

from mobile.heurestics.simple import is_apple_device, is_blackberry  

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
                 phone_number=None,
                 office_number=None,
                 latitude=None,
                 longitude=None):
    """
    
    Todo: handle encoding internally - currently pre-encoded strings assumed
    
    Create a vCard payload.

    http://vobject.skyhouseconsulting.com/usage.html
    
    http://svn.osafoundation.org/vobject/trunk/vobject/vcard.py
    
    http://www.ietf.org/rfc/rfc2426.txt
    
    http://en.wikipedia.org/wiki/VCard
    
    TEL;TYPE=WORK,VOICE:(111) 555-1212
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
        j.org.value = ["xxx"]
        
    
    if phone_number:
        j.add("tel")
        j.tel.value = phone_number
        j.tel.type_param = ["WORK","MOBILE"] 
    #if office_number:
    #    j.add('TEL')
    #    j.TEL.value = office_number
    #    j.TEL.value = ["WORK", "OFFICE"]    
    if latitude and longitude:
        # Not supported yet
        pass
            
    return j.serialize()

    
def is_vcard_supported(request):
    """
    @return: True if the device which made HTTP request can support HTTP downlodable vCards
    """
    if is_apple_device(request) or is_blackberry(request):
        return False
    
    return True
    