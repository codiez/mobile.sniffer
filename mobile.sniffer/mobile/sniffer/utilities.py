"""

    Misc. utilities to deal with HTTP user agent sniffing

"""
import md5

def get_environ(request):
    """ Cross-python framework compatible way to extract HTTP headers from the request object.


    @return: Dict of HTTP headers
    """

    if hasattr(request, "environ"):
        # WSGI
        return request.environ
    elif hasattr(request, "META"):
        # Django
        return request.META
    elif hasattr(request, "other"):
        # ZServer
        return request.other

    raise RuntimeError("Unknown HTTP request class:" + str(request.__class__))

def get_user_agent(request):
    """ Get the user agent string from the request.

    Deal with proxy pecularies and such.

    @param: WSGIRequest like object
    @return: Real user agent string
    """

    # We might have conflicting request types - assume request.environ is used
    environ = get_environ(request)

    agent = None

    if "HTTP_X_OPERAMINI_PHONE_UA" in environ:
        # Opera mini proxy specia case
        agent = environ["HTTP_X_OPERAMINI_PHONE_UA"]
    elif "HTTP_USER_AGENT" in environ:
        agent = environ["HTTP_USER_AGENT"]

    return agent

def is_low_end_phone(request):
    """ @return True: If the user is visiting the site using a crappy mobile phone browser.

    Low end phones have problem with:

        - Complex HTML syntax

        - Several images on the same page

        - Advanced CSS styles

        - Animations

        - Transparent backgrounds and alpha channel

        - 24-bit PNGs

    Before using the techniques above please filter them away for the crappy phones.
    This concerns at least Nokia Series 40 phones.

    Note that Opera Mini browser works smoothly on low end phones too...
    """

    # We assume all powerful mobile browsers are WebKit based
    user_agent = get_user_agent(request)

    if not user_agent:
        # Unit testing...
        return False

    user_agent = user_agent.lower()

    if "gecko" in user_agent:
        # Show high end version for desktop browser users
        return False

    if "opera" in user_agent:
        # Opera mini does its job well
        return False

    return not "webkit" in user_agent

def get_user_agent_hash(request):
    """ Helper function to get hashed user agent string.

    By adding this hash to URL you can make user agent specific URLs unique to caches,
    making cache problems disappear with image resizes. etc.

    Note: Do not persistent this hash. Hashing algorithm is subject to
    change any time.
    """
    user_agent =  get_user_agent(request)
    if user_agent:
        user_agent_md5 = md5.new(user_agent).hexdigest()
    else:
        # User agent will be None in unit tests
        user_agent_md5 = ""

    return user_agent_md5