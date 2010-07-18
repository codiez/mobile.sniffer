This package contains heurestics (rules-of-thumbs) for dealing with mobile phones in web systems.

Heurestics are divided to two categories

* mobile.heurestics.useragent: User agent based rules. Need *mobile.sniffer* package support.
  Heurestics are performed based on digged data from mobile agent user database.

* mobile.heurestics.simple: Rules are applied based on plain HTTP headers. User agent matching
  is self-contained and done dummily (if "iPhone" in user_agent...). 

Features
-------------

* Extracting user agent information from HTTP headers

* Detecting high-end and low-end mobile phones: simple.py

* Formatting phone number links (iPhone / WTAI): simple.py

* Creating Google Maps / waypoint links: poi.py / 

* Creating downloadable contact cards: vcard.py

* Generating correct HTTP headers and XHTML document type declaration: contenttype.py

* Detecting web crawlers in mobile mode (Googlebot): contenttype.py

* Downloadable video format detection RTSP / HTTP: video.py

We suggest you to take a look inside the Python source code and read the comments.

Dependencies
------------

* `vObject <http://vobject.skyhouseconsulting.com/>`_ library is used. 

If mobile.heurestic Python egg is installed via dependency aware installer (easy_install) 
the dependencies are automatically installed.

Source code
------------

Source code is available via Google Code.

* http://code.google.com/p/mobilesniffer/source/browse/#svn/trunk/mobile.heurestics

Beta software
-------------

This software is still in much development and aimed for advanced Python developers only.

Author
------

`mFabrik Research Oy <mailto:info@mfabrik.com>`_ - Python and Plone professionals for hire.

* `mFabrik web site <http://mfabrik.com>`_ 

* `mFabrik mobile site <http://mfabrik.mobi>`_ 

* `Blog <http://blog.mfabrik.com>`_

* `About Plone CMS <http://mfabrik.com/technology/technologies/content-management-cms/plone>`_ 


