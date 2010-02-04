"""

    Heurestics module unit test suite.

"""

import unittest

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"

from mobile.heurestics import vcard
from mobile.heurestics import contenttype

class MockRequest(object):
    """
    """

    def __init__(self):
        self.environ = {}

class BaseTestCase(unittest.TestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

    def setUp(self):
        pass


    def createMockRequest(self):
        """
        """
        # Create spoo
        return MockRequest()


class ContentTypeTestCase(BaseTestCase):
    """ No tests yet.
    """



class VCardTestCase(BaseTestCase):
    """ Test vCard generation options.
    """

    def test_double_phone_number(self):
        data = vcard.create_vcard(first_name="Mikko", last_name="Ohtamaa", mobile_number="+3581231234", landline_number="+35820100100")
        print data
        assert "100100" in data
        assert "1234" in data

    def test_title(self):
        data = vcard.create_vcard(first_name="Mikko", last_name="Ohtamaa", title="Mr.")
        print data
        assert "Mr." in data
        
    def test_double_link(self):
        data = vcard.create_vcard(first_name="Mikko", last_name="Ohtamaa", www_link="http://mfabrik.com", www_link_2="http://mfabrik.mobi")
        print data
        assert ".com" in data
        assert ".mobi" in data

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContentTypeTestCase))
    suite.addTest(unittest.makeSuite(VCardTestCase))
    return suite
