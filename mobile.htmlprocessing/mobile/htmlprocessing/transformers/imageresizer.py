"""

    Parse HTML and rewrite all images so that they go through mobile image resizer.
    
    This implementation does not have ties to any framework. Subclass this 
    and implement specific parts to support your framework image resizing facilities.

    http://www.mfabrik.com

"""

__license__ = "GPL 2"
__copyright__ = "2001 mFabrik Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@mfabrik.com>"
__docformat__ = "epytext"

from mobile.htmlprocessing.utilities import set_style, add_class

from basic import BasicCleaner

class ImageResizer(BasicCleaner):
    """
    1. Rewrite all image links to point to resized versions

    2. De-float images

    3. And missing alt="" tags if any

    Note that in non-trusted mode all style attributes get cleared.
    """
    
    def __init__(self, base_url, trusted=False):
        """ 
        @param base_url: For resolving relative image URLs  
        """
        BasicCleaner.__init__(self, trusted=trusted)
        self.base_url = base_url
        
        
    def rewrite(self, url):
        """ Rewrite <img> source URL.
    
        The actual implementation must override this method.
        
        @param: url as string
        @return: Image URL as it should
        """
        return url
    
    def needs_clearing(self, el):
        """ Check whether image must be defloated.
        
        The subclass may override this to have specific filtering.
        
        @return: True if <img> element must be defloated
        """
        return True
    
    def clear_floats(self, el):
        """ 
        """
        style = el.attrib.get("style", None)
        style = set_style(style, "float: none")
        el.attrib["style"] = style
    
    def get_processed_class(self, el):
        """
        @return: CSS class applied to all processed <img> elements
        """    
        return "mobile-resized"
    
    def add_processed_class(self, el):
        """ Mark <img> specially resized.
        """
        klass = el.attrib.get("class", None)
        klass = add_class(klass, self.get_processed_class(el))
        el.attrib["class"] = klass
    
    def process_img(self, doc, el):
        """ Process <img> tag in the source docu,ent.
        
        """
        self.add_alt_tags(el)
        
        src = el.attrib.get("src", None)
        if src:
            el.attrib["src"] = self.rewrite(src)
            
            # Remove explicit width declarations
            if "width" in el.attrib:            
                del el.attrib["width"]

            if "height" in el.attrib:            
                del el.attrib["height"]

            
        if self.needs_clearing(el):
            self.clear_floats(el)

        
        self.add_processed_class(el)