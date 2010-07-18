.. contents :: 

Introduction
------------

``mobile.htmlprocessing`` is a Python package providing utilities to sanitize 
arbitrary HTML content for outputting it to mobile devices.

Features
--------

* Rewrite <img> tags so that images are resized for mobile viewing

* Make arbitraty input HTML to valid XHTML to more compatible with mobile phones

* Enforce empty ALT text on images missing ALT attribute

* Protect against Cross-Site Scripting Attacks (XSS) and other nastiness, as provided by
  `lxml.html.clean  <http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html>`_. 
  Both trusted HTML and non-trusted HTML processing modes are supported.

* Unicode compliant - eats funky characters

This is a framework library which is designed to work with any web server or Python based CMS system.
It allow rewrites HTML. You need to subclass and specialize provided base classes to match with your CMS
paradigms. For examples, see `Go Mobile for Plone <http://pypi.python.org/pypi/gomobile.mobile/>`_
CMS add-on product.

Requirements
------------

* Python 2.4+

* `lxml <http://pypi.python.org/pypi/lxml/>`_

Usage
-----

Please see example code in unit tests.

Unit tests
----------

Put mobile.htmlprocessing to your PYTHONPATH.

Run unit tests normally like::

	python tests/test_image.py

See also
--------

* `Go Mobile for Plone project <http://pypi.python.org/pypi/gomobile.mobile/>`_

* http://en.wikipedia.org/wiki/XHTML_Mobile_Profile

* http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html

* `W3C XHTML mobile validator <http://validator.w3.org/mobile/>`_

Source code
------------

Source code is available via Google Code.

* http://code.google.com/p/mobilesniffer/source/browse/#svn/trunk/mobile.htmlprocessing

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


