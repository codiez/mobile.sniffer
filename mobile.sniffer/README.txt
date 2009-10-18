Introduction
------------

mobile.sniffer is cross-web-framework, cross-device data provider, Python framework for sniffing mobile handset properties.

When rendering web pages for mobile phones one must deal with varying handset features: different screen sizes and shapes, different supported file formats, different sets of web browser features. This library is the ultimate solution to deal with this complexity.

Support different sniffing patterns (HTTP user agent, WAP headers) and different databases (DeviceAtlas, Apex Vertex, WAP profiles).

Django, WSGI and Zope/Plone compatible.

Features
--------

* Able to source data from multiple sniffing backends leading better handset coverage

* Automatically download, parse and cache complex RDF based WAP profiles

* Very convenient Python API designed by professionals

* Maintained

* Open source

* Unit test coverage

Sniffing backends
-----------------

||ÊBackend ||ÊDependencies ||ÊFeatures ||
||Apex Vertex || Django || 1000+ handsets, Northern European weighted, good streaming data. Fuzzy user agent matching to deal with software revision specific user agents. Can be bought from Twinapex.||
||ÊDeviceAtlas ||Êzope.testbrowser (optional) ||Ê4000+ handsets. mobile.sniffer provides automatic download and deploment for proprietary DeviceAtlas Python APIs and data files. You need only a valid DeviceAtlas account. Can be bought from mobiForge. ||
||ÊWAP profiles ||ÊDjango, rdflib ||ÊAuthoritative source. Many handset manufacturers publish WAP profiles in HTTP headers. They are XML files describing the device properties. If the profile header is present, the profile is downloaded, cached and parsed. Free. ||

Installation
------------

mobile.sniffer is distributed as Python egg in PyPi repository.
The usual method to install Python eggs is easy_install command.

Simple (Unix version)::

	sudo easy_install mobile.sniffer

Automatic installers
--------------------

Proprietary handset databases do not publicly distribute their APIs or data. mobile.sniffer deals with the problem by automatic installation wrappers. Also, these handset database APIs are not open source compatible which makes it further difficult to use them in open source projects. Instead of manually download and set up bunch of files each time you deploy your code on a new server, just make call to one magical Python function which will take care of all of this for you.

Architecture
------------

* Modular structure with generic call interface across different sniffing backends

* Different sniffers can be chained for better accuracy

* Uses very well documented DeviceAtlas property names as keys for property queries

Usage examples
--------------

Simple example
======================

Example::

	from mobile.sniffer.apexvertex.installer import install_apex_vertex
	from mobile.sniffer.apexvertex.sniffer import ApexVertexSniffer

	# For this project, we source our mobile handset data from
	# Apex Vertex database
	sniffer = ApexVertexSniffer()

	def init():
	    # Populate SQL database with provded handset information -
	    # you only need to do this when handset data is updated
	    install_apex_vertex("mydata.json")

	def render_page(request):
	    # Request can be Django, WSGI or Zope HTTPRequest object
	    user_agent = sniffer.sniff(request)

	    if user_agent == None:
	        # No match in the handset database,
	        return render_unknown_mobile_phone_page()

	    width = user_agent.get("usableDisplayWidth")
	    height = user_agent.get("usableDisplayHeight")
	    has_video_link = user_agent.get("stream.3gp.h263") # Does the handset support our 3GP video clip

	    return render_mobile_page(width, height, has_video_link)


Chained example
====================

Use all available handset information sources to accurately get device data.
Matching is done on property level - if one data source lacks the property information the next data source is tried. Finally if the handset is unknown, but it publishes WAP profile information, the profile is downloaded and analyzed and saved for further requests.

Example::

    from mobile.sniffer.chain import ChainedSniffer
    from mobile.sniffer.apexvertex.sniffer import ApexVertexSniffer
    from mobile.sniffer.wapprofile.sniffer import WAPProfileSniffer
    from mobile.sniffer.deviceatlas.sniffer import DeviceAtlasSniffer

    # Create all supported sniffers
    da = DeviceAtlasSniffer(da_api_file)
    apex = ApexVertexSniffer()
    wap = WAPProfileSniffer()

    # Preferred order of sniffers
    sniffer = ChainedSniffer([apex, da, wap])

    ua = sniffer.sniff(request) # Sniff HTTP_USER_AGENT, HTTP_PROFILE and many other fields
    property = ua.get("usableDisplayWidth") # This will look up data from all the databases in the chain


Developer for you by [http://www.twinapex.com Twinapex]Êand open source community.




