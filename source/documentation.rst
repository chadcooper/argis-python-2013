Using Python to create documentation
====================================

How should I document my code?
-------------------------------

This set of html files that compose the workshop notes were created with a 
documentation tool called `Sphinx`_. Sphinx uses `reStructuredText`_ as its markup 
language and Python translates it to HTML (among other formats). 

Look over to the left of this page you are reading in the sidebar under the 
Table of Contents where it says "This page". Click on "Show Source" - what you 
will see is the reStructuredText that I wrote that Sphinx in turn generated into 
the html content. 

Before we talk about Sphinx, let's discuss package managers
-----------------------------------------------------------

Python doesn't ship with a package manager. Which sucks. So how do you install 
3rd party packages? First you have to install the installer.

.. note:: 

   3rd party packages are packages or libraries that are not part of the 
   Python standard library. They are authored by various people and put out 
   into the public domain for use. Since they don't come packaged with Python, 
   you have to install them somehow. This is one thing that package managers 
   do.
   
Old skool
+++++++++
   
* ``easy_install`` - yeah, it installs stuff, but easy?
* ``$ python setup.py install`` - usually works ok, but ininstalling isn't easy
* Windows installation executables - work ok, but kinda clunky

New skool
+++++++++

``pip``

* super-easy for installing packages

    ``$ pip install some-package``
    
* super-easy unistall that *actually works*

    ``$ pip uninstall some-package``

* *Not* so intuitive to install it, ironically

Installing pip
++++++++++++++

The easiest way for us to install pip is to first install setuptools, which 
pip is dependendt upon. Get a Windows installer here and run it:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools

Next, get the pip installer here and run it:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip

Now, assuming the installs went properly and our ``Path`` variable is properly 
set, you should be able to:

.. code-block:: bash

   C:\Users\class5user>pip

   Usage:
     pip <command> [options]

   Commands:
     install                     Install packages.
     uninstall                   Uninstall packages.
     freeze                      Output installed packages in requirements format.
     list                        List installed packages.
     show                        Show information about installed packages.
     search                      Search PyPI for packages.
     wheel                       Build wheels from your requirements.
     zip                         Zip individual packages.
     unzip                       Unzip individual packages.
     bundle                      Create pybundles.
     help                        Show help for commands.

   General Options:
     -h, --help                  Show help.
     -v, --verbose               Give more output. Option is additive, and can be
                                 used up to 3 times.
     -V, --version               Show version and exit.
     -q, --quiet                 Give less output.
     --log <file>                Log file where a complete (maximum verbosity)
                                 record will be kept.
     --proxy <proxy>             Specify a proxy in the form
                                 [user:passwd@]proxy.server:port.
     --timeout <sec>             Set the socket timeout (default 15 seconds).
     --exists-action <action>    Default action when a path already exists:
                                 (s)witch, (i)gnore, (w)ipe, (b)ackup.
     --cert <path>               Path to alternate CA bundle.

   C:\Users\class5user>

How to install Sphinx and build docs
------------------------------------

There are plenty of tutorials out there, I like `this one`_. Sphinx is easy to 
install and get started with.

1. Skip their installation step and instead just do this:

   ``pip install sphinx``
   
2. Make a directory for our documentation, ``cd`` into it, then setup sphinx:

   ``C:\Users\class5user\ar-gis-python>mkdir docs``

   ``C:\Users\class5userar-gis-python>cd docs``
   
   `` C:\Users\class5user\ar-gis-python\docs>sphinx-quickstart``
   
   During ``sphinx-quickstart``, just hit enter and take the defaults fo now.
  
3. In Windows Explorer, go to your ``docs`` directory and check it out. Open 
   up ``index.rst`` in Notepad or Notepad2 if we installed it. Add the call to 
   ``page1.rst`` like below:  

   .. code-block:: rst
   
      .. Jimmy documentation master file, created by
         sphinx-quickstart on Sun Sep 08 19:53:23 2013.
         You can adapt this file completely to your liking, but it should at least
         contain the root `toctree` directive.

      Welcome to Jimmy's documentation!
      =================================

      Contents:

      .. toctree::
         :maxdepth: 2

         page1.rst

      Indices and tables
      ==================

      * :ref:`genindex`
      * :ref:`modindex`
      * :ref:`search`

4. In the ``docs`` dir, create a file called ``page1.rst``. Open it up in the 
   text editor and write something like so:
   
   .. code-block:: rst
   
      Here is the first header of page 1
      ==================================

      .. code-block:: python

         def foo():
             return bar

5. Finally, build your docs:

   .. code-block:: bash
     
      C:\Users\class5user\ar-gis-python\docs>sphinx-build . doc
      
6. From the ``docs`` directory, open up ``index.html`` in your browser.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _this one: http://scienceoss.com/use-sphinx-for-documentation/