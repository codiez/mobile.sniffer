"""
    
    Determine which video formats to server.
    
    
    Note: This heurestics might not be accurate as Wurlf enty digging, but they cover "almost all" cases...
    
"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "2010 mFabrik Research Oy"
__license__ = "GPL"
__docformat__ = "epytext"

from mobile.heurestics import simple

def support_rtsp_video(request):
    """
    """

    if simple.is_iphone(request):
        return False
        
    return True
    

def support_http_video(request):
    """ Does phone support HTTP video playback.
    
    Not necessarily progressive.
    """
    
    if simple.is_iphone(request):
        return True
    
    return False

def get_preferred_video_protocol(request):
    """
    
    @return: "rtsp" or "http" according to how the handset video should be server. None if video is not supported.
    """
    
    if support_rtsp_video(request):
        return "rtsp"
    
    if support_http_video(request):
        return "http"
    
    return None
    