from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='mobile.heurestics',
      version=version,
      description="A collections of rules-of-thumbs for dealing with mobile phones in web systems",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='mobile video vcard sniffer map javascript phone',
      author='Mikko Ohtamaa',
      author_email='research@mfabrik.com',
      url='http://mfabrik.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'vobject' # For manipulating vCards
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
