.. contents ::

Introduction
------------

mobile.htmlprocessing provides utilities to sanitize arbitary HTML for mobile output.

The code will also filter possible malicious code in external feed content, like <script> tags.

Requirements
------------

* Python 2.4

* `lxml <http://pypi.python.org/pypi/lxml/>`_

This package has no dependencies to Plone or Go Mobile and can be used with any Python code.

Features
--------

* Rewrite <img> tags so that images are resized for mobile viewing

* Make arbitary input HTML to valid XHTML to more compatible with mobile phones

* Enforce empty ALT text on images missing ALT attribute

* Protect against Cross-Site Scripting Attacks (XSS) and other nastiness, as provided by
  `lxml.html.clean  <http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html>`_

* Unicode compliant - eats funky characters

* Both trusted HTML and non-trusted HTML (may contain <script> and <iframe> etc.) 
  modes


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

* `Plone GoMobile project <http://pypi.python.org/pypi/gomobile.mobile/>`_

* http://en.wikipedia.org/wiki/XHTML_Mobile_Profile

* http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html

* `W3C XHTML mobile validator <http://validator.w3.org/mobile/>`_

* `mobiReady <http://mobiready.com/>`_

Author
------

`mFabrik Research Oy <mailto:info@mfabrik.com>`_ - Python and Plone professionals for hire.

* `mFabrik web site <http://mfabrik.com>`_ 

* `mFabrik mobile site <http://mfabrik.mobi>`_ 

* `Blog <http://blog.mfabrik.com>`_
