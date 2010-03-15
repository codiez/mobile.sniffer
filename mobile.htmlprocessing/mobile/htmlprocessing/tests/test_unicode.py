# -*- coding: utf-8 -*-

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

import unittest

from mobile.htmlprocessing.transformers.basic import fix_html

class UnicodeTestCase(unittest.TestCase):
    
    def test_unicode(self):
        html = u'<div>ÅÄÖ</div>'
        output = fix_html(html) 
        
        output = output.decode("utf-8")
               
        self.assertEqual(output, u'<div>ÅÄÖ</div>', "Got:" + output)


def test_suite():    
    return unittest.makeSuite(UnicodeTestCase)
        
if __name__ == '__main__':
    unittest.main()
        