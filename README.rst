django-runscript
=================

Synopsis
--------
A management command for running Python scripts, from the commandline, while
providing access to the Django environment.


Code Example
------------
From a shell::

    $ manage runscript path/to/my_script.py
    

Installation
------------
`pip install -e git+https://github.com/OaklandPeters/django-runscript#egg=django-runscript`

Then add `runscript` to the `INSTALLED_APPS` of your Django settings file::

    INSTALLED_APPS = INSTALLED_APPS + ('runscript', )


Contributors
-------------
Oakland John Peters <oakland.peters@gmail.com>


License
---------
Available under the ``MIT license <http://opensource.org/licenses/MIT/>`_.

Copyright (c) 2014, Oakland John Peters.
