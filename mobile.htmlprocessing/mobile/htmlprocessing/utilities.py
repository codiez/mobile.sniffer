"""

    HTML processing utilities.
    
    http://www.mfabrik.com

"""

__license__ = "GPL 2"
__copyright__ = "2001 mFabrik Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@mfabrik.com>"
__docformat__ = "epytext"


def add_style(style_string, new_style):
    """ Appends a new style to HTML style string.
    
    @param new_style: Style to append e.g. "float: none"
    
    @param style_string: The existing style attribute content or None if does not exist
    """
    
    if style_string:
        new = style_string + ";"
    else:
        new = ""
        
    new += new_style

    return new 

def add_class(class_string, new_class):
    """
    Append new CSS class to existing class string
    """
    if class_string:
        new = class_string + " "
    else:
        new = ""
        
    new += new_class

    return new   