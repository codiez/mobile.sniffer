"""

     Wurlf based user agent sniffing backend.

     http://pypi.python.org/pypi/pywurfl/

"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.fi>"
__copyright__ = "2009 Twinapex Research"
__license__ = "GPL"
__docformat__ = "epytext"


import os, sys

from mobile.sniffer import base

from pywurfl.algorithms import JaroWinkler

class WurlfSniffer(base.Sniffer):
    """

    Native Wurlf capabilities are listed here: http://wurfl.sourceforge.net/help_doc.php
    """

    def __init__(self, database_file=None):
        """

        @param database_file: Path to Wurlf XML file or None to use internal database
        """

        if database_file is None:
            # Import devices from the internal database shipped
            # with the source code
            from wurfl import devices
            self.devices = devices
        else:
            raise NotImplementedError("TODO")

        # Set search algorithm
        self.search = JaroWinkler(accuracy=0.85)

    def sniff(self, request):
        """ Look up handset from DeviceAtlas database using HTTP_USER_AGENT as a key """
        agent = self.get_user_agent(request)

        if not agent:
            return None

        device = self.devices.select_ua(agent, search=self.search)

        return UserAgent(device)

class UserAgent(base.UserAgent):
    """ Wurfl record wrapper.
    """

    def __init__(self, device_object):

        # internal DA properties object
        self.device_object = device_object

    def get(self, name):
        """ Get property in DeviceAtlas compatible way.

        @param name: Property name, like usableDisplayWidth
        @return: Property value, string converted to a real object

        """

        if name == "is_wireless_device":
            return self.device_object.is_wireless_device

        if not self.device_object.is_wireless_device:
            # TODO: Make generic resolution
            # for identifying web browsers with width fallback
            # otherwise returned values for usable display with will be
            # the lowest common denominator (90 x 35)
            return None

        if name == "usableDisplayWidth":
            return self.device_object.max_image_width
        elif name == "usableDisplayHeight":
            return self.device_object.max_image_height
        else:
            return None
