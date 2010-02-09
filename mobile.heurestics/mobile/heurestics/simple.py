"""

    Simple heurestics rules.

"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 Twinapex Research"
__license__ = "GPL"
__docformat__ = "epytext"


from mobile.sniffer.utilities import get_user_agent

def is_low_end_phone(request):
    """ @return True: If the user is visiting the site using a crappy mobile phone browser.

    Low end phones have problem with:

        - Complex HTML syntax

        - Several images on the same page

        - Advanced CSS styles

        - Animations

        - Transparent backgrounds and alpha channel

        - 24-bit PNGs

    High end phones:

    * Firefox (Gecko based) browseres

    * Webkit based browsers

    Low end phones:

    * All other

    Before using the techniques above please filter them away for the crappy phones.
    This concerns at least Nokia Series 40 phones.

    Note that Opera Mini browser works smoothly on low end phones too...
    """

    # We assume all powerful mobile browsers are WebKit based
    user_agent = get_user_agent(request)

    if not user_agent:
        # Unit testing...
        return False

    user_agent = user_agent.lower()

    if "gecko" in user_agent:
        # Show high end version for desktop browser users
        return False

    if "maemo" in user_agent:
        # Show high end version for desktop browser users
        return False

    if "opera" in user_agent:
        # Opera mini does its job well
        return False
    
    if "fennec" in user_agent or "maemo" in user_agent:
        return True

    return not "webkit" in user_agent

def is_high_end_phone(request):
    """ Can phone handle complex web pages"""
    return not is_low_end_phone(request)

def is_javascript_supported(request):
    """ Does phone have meaningful Javascript support

    @param request: HTTP request object (WSGI/Zope/Django)
    """
    user_agent = get_user_agent(request)

    if "opera" in user_agent:
        # Opera mini javascript support is
        # not good enough to be useable as it is thin client
        return False

    return is_high_end_phone(request)

def is_iphone(request):
    """
    
    @deprecated: Use is_apple_device() method
    
    @param request: HTTP request object (WSGI/Zope/Django)
    """
    return is_apple_device(request)

def is_apple_device(request):
    """    
    @return: True if the HTTP request was made by iPod/iPhone/iPad
    
    """    
    user_agent = get_user_agent(request)

    return ("iPhone" in user_agent) or ("iPod" in user_agent) or ("iPad" in user_agent)    

def is_blackberry(request):
    """ Is the device which makde HTTP request Blackberry like
     
    @param request: HTTP request object (WSGI/Zope/Django)
    """

    user_agent = get_user_agent(request)
    return "blackberry" in user_agent.lower()

def is_android(request):
    """ Is the device which makde HTTP request Blackberry like
     
    @param request: HTTP request object (WSGI/Zope/Django)
    """

    user_agent = get_user_agent(request)
    return "android" in user_agent.lower()


def format_phone_number_href(request, human_readable_number):
    """

    http://www.searchenginepeople.com/blog/iphone-search-result-optimization-tip-1-phone-numbers-in-meta-tags.html

    @param request: HTTP request object (WSGI/Zope/Django)

    @param human_readble_number: Phone number in human readable format - may contain spaces and such
    """

    allowed = "+*0123456789"

    # Make phone number digits only
    plain_number = [ digit for digit in human_readable_number if digit in allowed ]
    plain_number = "".join(plain_number) # convert list back to string

    if is_iphone(request):
        href = "tel:" + plain_number
    else:
        href = "wtai://wp/mc;" + plain_number

    return href


