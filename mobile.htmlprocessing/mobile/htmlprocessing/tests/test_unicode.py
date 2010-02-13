# -*- coding: utf-8 -*-

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"
__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__author_url__ = "http://www.twinapex.com"

import unittest

from mobile.htmlprocessing.transformers.alttagger import fix_images

class UnicodeTestCase(unittest.TestCase):
    
    def test_unicode(self):
        html = u'<div>ÅÄÖ</div>'
        output = fix_images(html)        
        self.assertEqual(output, u'<div>ÅÄÖ</div>', "Got:" + output)
        
if __name__ == '__main__':
    unittest.main()
        