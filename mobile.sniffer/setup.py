from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mobile.sniffer',
      version=version,
      description="Generic Python framework for mobile user agent detection",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mobile django plone user-agent http',
      author='Mikko Ohtamaa',
      author_email='mikko.ohtamaa@twinapex.fi',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['mobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
