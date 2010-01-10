"""

    Mobile content type helpers. Get HTTP content type and doctype according 
    to what the handset asks for.
    
    
    TODO: Only supports XHTML basic for now.

    http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension

"""

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

MOBILE_CONTENT_TYPES = [
    "application/vnd.wap.xhtml+xml", 
    "application/xhtml+xml"
]


def get_suggested_content_type(request):
    """ Get content type for XHTML mobile profile documents.

    @param request: Request

    @return: Content type which should be used for response, None if should not be modified
    """

    accepted = None

    # Go through possibilities
    for option in accepted:
        if option.lower() in MOBILE_CONTENT_TYPES:
            return option

    return None

def get_html_docstring(request):
    """

    @return: Which docstring should be used
    """
    
def get_content_type_and_doctype(request):
    """ TODO: hardcoded for now
    
    http://www.google.com/support/webmasters/bin/answer.py?hl=fi&answer=40348
    
    @param accepted: HTTP Accepted header 
    """
    return "Content-Type: application/xhtml+xml;charset=UTF-8", '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.0//FI" "http://www.w3.org/TR/xhtml-basic/xhtml-basic10.dtd">'
    