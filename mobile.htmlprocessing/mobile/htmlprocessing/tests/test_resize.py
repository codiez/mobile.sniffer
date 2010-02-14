# -*- coding: utf-8 -*-

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

import urllib
import unittest

from mobile.htmlprocessing.transformers.imageresizer import ImageResizer

DUMMY_RESIZE_VIEW="http://localhost/@@resizer?url="

class MockResizer(ImageResizer):
    """
    """
    
    def rewrite(self, url):
        """ Return dummy URL for testing
        """
        return DUMMY_RESIZE_VIEW + urllib.quote_plus(url)

class ResizerTestCase(unittest.TestCase):
    """ Test <img> tag handling
        
    """    
    
    def transform(self, html):
        resizer = MockResizer(base_url=None, trusted=True)
        return resizer.process(html)
    
    def test_simple(self):
        """ Check that images receive empty alt tag if one is missing """
        
        html = '<img src="http://www.foobar.com">'
        output = self.transform(html)        
        self.assertEqual(output, '<img src="http://localhost/@@resizer?url=http%3A%2F%2Fwww.foobar.com" alt="" style="float: none" class="mobile-resized"/>', "Got:" + output)
                
    def test_alt(self):
        """ Check that existing ALT attribute stays untouched """
        html = '<img src="http://www.foobar.com" alt="bar">'
        output = self.transform(html)        
        self.assertTrue('alt="bar"' in output, "Got:" + output)
        
    def test_got_css_class(self):
        html = '<img src="http://www.foobar.com" ALT="bar">'
        output = self.transform(html)        
        self.assertTrue('class="mobile-resized"' in output, "Got:" + output)

    def test_got_no_float(self):
        html = '<img src="http://www.foobar.com" ALT="bar">'
        output = self.transform(html)        
        self.assertTrue('style="float: none"' in output, "Got:" + output)

    def test_process_existing_float(self):
        html = '<img src="http://www.foobar.com" ALT="bar" style="float: left">'
        output = self.transform(html)        
        self.assertFalse('left' in output, "Got:" + output)
        self.assertTrue('float: none' in output, "Got:" + output)
        
    def test_process_existing_float_multi_style(self):
        html = '<img src="http://www.foobar.com" style="float: left; border: 1px solid black" ALT="asdasdbar" />'
        output = self.transform(html)        
        self.assertTrue('solid black' in output, "Got:" + output)
        self.assertFalse('left' in output, "Got:" + output)

    def test_process_existing_float_hyper_multi_style(self):
        html = '<img src="http://www.foobar.com" style="display: none; float: left; border: 1px solid black" ALT="asdasdbar" />'
        output = self.transform(html)        
        self.assertTrue('solid black' in output, "Got:" + output)
        self.assertFalse('left' in output, "Got:" + output)
        self.assertTrue('display: none' in output, "Got:" + output)
        
def test_suite():    
    return unittest.makeSuite(ResizerTestCase)

                        
if __name__ == '__main__':
    unittest.main()
        