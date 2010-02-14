# -*- coding: utf-8 -*-

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

import unittest

from mobile.htmlprocessing.transformers.basic import fix_html

class ImageTestCase(unittest.TestCase):
    """ Test <img> tag handling
        
    """    
    
    def test_add_alt_tag(self):
        """ Check that images receive empty alt tag if one is missing """
        
        html = '<img src="http://www.foobar.com">'
        output = fix_html(html)        
        self.assertEqual(output, '<img src="http://www.foobar.com" alt=""/>', "Got:" + output)
                
    def test_no_modify_existing_alt(self):
        """ Check that existing ALT attribute stays untouched """
        html = '<img src="http://www.foobar.com" alt="bar">'
        output = fix_html(html)        
        self.assertEqual(output, '<img src="http://www.foobar.com" alt="bar"/>', "Got:" + output)
        
    def test_no_modify_existing_alt_caps(self):
        html = '<img src="http://www.foobar.com" ALT="bar">'
        output = fix_html(html)        
        self.assertEqual(output, '<img src="http://www.foobar.com" alt="bar"/>', "Got:" + output)


def test_suite():    
    return unittest.makeSuite(ImageTestCase)

if __name__ == '__main__':
    unittest.main()
        