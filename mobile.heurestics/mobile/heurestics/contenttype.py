"""

    XXXX - this code is not finished - DO NOT USE

    Mobile content type helpers.


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