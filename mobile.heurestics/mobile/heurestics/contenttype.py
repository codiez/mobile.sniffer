"""

    Mobile content type helpers. Get HTTP content type and doctype according 
    to what the handset asks for.
    
    
    TODO: Only supports XHTML basic for now.

    http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension
    
    http://en.wikipedia.org/wiki/XHTML_Mobile_Profile

"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 mFabrik Research Oy"
__license__ = "GPL v2"
__docformat__ = "epytext"

from mobile.sniffer.utilities import get_user_agent, get_environ

MOBILE_CONTENT_TYPES = [
    "application/vnd.wap.xhtml+xml", 
    "application/xhtml+xml"
]

# User agent string snippets which identify XHTML aware bots   
# All owercased
# Note that this should cover BOTH web and mobile bots, so that web bots know they are crawling a mobile site
bots_know_about_mobile_xhtml = ["googlebot"]


#def get_suggested_content_type(request):
#    """ Get content type for XHTML mobile profile documents.
#
#    @param request: Request
#
#    @return: Content type which should be used for response, None if should not be modified
#    """
#
#    accepted = None
#
#    # Go through possibilities
#    for option in accepted:
#        if option.lower() in MOBILE_CONTENT_TYPES:
#            return option
#
#    return None

#def get_html_docstring(request):
#    """
#
#    @return: Which docstring should be used
#    """

def need_xhtml(request):
    """ Determine whether HTML'ish request should be served as XHTML.
    
    1. The HTTP_ACCEPT header is set correctly
    
    2.  
    
    Note: This should be done for bots only. See reasons in Developer Manual, XHTML section.
    """
    
    environ = get_environ(request)
    
    header = environ.get("HTTP_ACCEPT", None)
    if not header:
        return False
    
    if not "application/xhtml+xml" in header:
        return False

    ua = get_user_agent(request)
    if ua:
        ua = ua.lower()
        for bot in bots_know_about_mobile_xhtml:
            if bot in ua:
                return True
        
    return False

def get_content_type_and_doctype(request):
    """ TODO: hardcoded for now
    
    http://www.google.com/support/webmasters/bin/answer.py?hl=fi&answer=40348
    
    For Google, give XHTML MP, for other, give real HTML.
    
    @param accepted: HTTP Accepted header 
    """
    
    # hack hack hack
    if need_xhtml(request):
        return "application/xhtml+xml;charset=UTF-8", '<?xml version="1.0" encoding="utf-8" ?><!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN" "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">'
        
    return "text/html;charset=UTF-8", '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
    

#def get_start(request, lang):
#    return get_content_type_and_doctype(request) + get_html_tag(request, lang)
    
