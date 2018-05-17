==============
ploneedu.theme
==============

A theme for the latest PloneEdu site. `PloneEdu`_ is a collaboration of 
educational institutions using Plone.


Introduction
============

*PloneEdu Theme* is an installable Plone Theme developed by `PloneEdu`_ people 
using the **theming** and **packaging** features available in `plone.app.theming`_.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/ploneedu.theme/raw/master/screenshot.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support for clean uninstallation.


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``ploneedu.theme`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        ploneedu.theme


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'ploneedu.theme',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Add-ons control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/collective/ploneedu.theme/issues
- Source Code: https://github.com/collective/ploneedu.theme


License
=======

The project is licensed under the GPLv2.


Credits
-------

This theme was designed by `Mark Corum`_ and implemented by `Rob Porter`_.


Contributors
------------

- T\. Kim Nguyen (nguyen at gmail dot com).
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).


.. _`PloneEdu`: https://plone.org/edu
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Mark Corum`: https://twitter.com/markcorum
.. _`Rob Porter`: https://twitter.com/robzonenet
