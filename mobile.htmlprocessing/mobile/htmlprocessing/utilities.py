"""

    HTML processing utilities.
    
    http://www.mfabrik.com

"""

__license__ = "GPL 2"
__copyright__ = "2001 mFabrik Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@mfabrik.com>"
__docformat__ = "epytext"


def set_style(style_string, new_style):
    """ Appends a new style to HTML style string.
    
    @param new_style: Style to append e.g. "float: none"
    
    @param style_string: The existing style attribute content or None if does not exist
    """
    
    
    if style_string:
    
        new_style_css_directive = new_style.split(":")[0] 
    
        def filter(x):
            """ Filter out the existing CSS directive for the style
            """
            x = x.strip()
            #print "Matching " + x + " " + new_style_css_directive
            if x.startswith(new_style_css_directive):
                return False
            return True
                
        parts = style_string.split(";")
        style_string = ";".join([ part for part in parts if filter(part) == True ])
    
        # Do we have any more elements left?
        if len(style_string) > 0:
            new = style_string + ";"
        else:
            new = ""
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