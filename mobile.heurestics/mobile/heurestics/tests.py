"""

    Heurestics module unit test suite.

"""

import unittest

__license__ = "GPL 2"
__copyright__ = "2009 Twinapex Research"

class MockRequest(object):
    """
    """

    def __init__(self):
        self.environ = {}

class BaseTestCase(unittest):
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
    """
    """

    def test_wml(self):
        """
        """
        request = self.createMockRequest()
        request.environ["accept"] = "application/vnd.wap.xhtml+xml"

        suggested = get_suggested_content_type(request)
        self.assertEqual(suggested, "application/vnd.wap.xhtml+xml")

    def test_xhtml(self):
        """
        """


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContentTypeTestCase))
    return suite
