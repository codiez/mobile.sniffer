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

from mobile.htmlprocessing.utilities import add_style, add_class

from basic import BasicCleaner

class ImageResizer(BasicCleaner):
    """
    1. Rewrite all image links to point to resized versions

    2. De-float images

    3. And missing alt="" tags if any
    """
    
    def __init__(self, base_url):
        """ 
        @param base_url: For resolving relative image URLs  
        """
        self.base_url
        
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
        style = add_style(style, "float: none")
        el.attrib.set("style", style)
    
    def get_processed_class(self, el):
        """
        @return: CSS class applied to all processed <img> elements
        """    
        return "mobile-resized"
    
    def add_processed_class(self, el):
        """
        """
        klass = el.attrib.get("class", None)
        klass = add_class(klass, self.get_processed_class(el))
        el.attrib.set("class", klass)
    
    def process_img(self, doc, el):
        """
        
        """
        self.add_alt_tags(el)
        
        src = el.attrib.get("src", None)
        if src:
            el.attrib[src] = self.rewriter(src)
            
        if self.needs_clearing(el):
            self.clear_floats(el)

        self.add_processed_class(el)