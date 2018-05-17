from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ploneedu.theme',
      version=version,
      description='PloneEdu Theme, is an installable Diazo theme for Plone 4',
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone diazo theme plonetheme ploneedu cms',
      author='Rob Porter',
      author_email='robzonenet@gmail.com',
      maintainer='T. Kim Nguyen',
      maintainer_email='nguyen@plone.org',
      url='https://github.com/collective/ploneedu.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneedu'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.responsivetheme',
          'Products.EasyAsPiIE',
          'Products.ContentWellPortlets',
          'z3c.jbot>=0.6.0',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
