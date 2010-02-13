# -*- coding: utf-8 -*-

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

import urllib
import unittest

from mobile.htmlprocessing.transformers.imageresizer import ImageResizer

DUMMY_RESIZE_VIEW="http://localhost/@@resizer?url="

class TestResizer(ImageResizer):
    """
    """
    
    def rewrite(self, url):
        """ Return dummy URL for testing
        """
        return DUMMY_RESIZE_VIEW + urllib.quote_plus(url)

class ImageTestCase(unittest.TestCase):
    """ Test <img> tag handling
        
    """    
    
    def transform(self, html):
        resizer = TestResizer(base_url=None)
        return resizer.process(html)
    
    def test_simple(self):
        """ Check that images receive empty alt tag if one is missing """
        
        html = '<img src="http://www.foobar.com">'
        output = self.transform(html)        
        self.assertEqual(output, '<img src="http://www.foobar.com" alt=""/>', "Got:" + output)
                
    def test_alt(self):
        """ Check that existing ALT attribute stays untouched """
        html = '<img src="http://www.foobar.com" alt="bar">'
        output = self.transform(html)        
        self.assertTrue('alt="bar"' in output, "Got:" + output)
        
    def test_got_css_class(self):
        html = '<img src="http://www.foobar.com" ALT="bar">'
        output = self.transform(html)        
        self.assertTrue('class="mobile-resizer"' in output, "Got:" + output)

    def test_got_no_float(self):
        html = '<img src="http://www.foobar.com" ALT="bar">'
        output = self.transform(html)        
        self.assertTrue('style="float: none"' in output, "Got:" + output)
                        
if __name__ == '__main__':
    unittest.main()
        