from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mobile.sniffer',
      version=version,
      description="Generic framework for mobile user agent detection",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mobile django plone user-agent http',
      author='Mikko Ohtamaa',
      author_email='mikko.ohtamaa@twinapex.fi',
      url='http://www.twinapex.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['mobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
