============
Installation
============

Python
======

**Python** is a widely used `high-level <https://en.wikipedia.org/wiki/High-level_programming_language>`_,
`general-purpose <https://en.wikipedia.org/wiki/General-purpose_programming_language>`_,
`interpreted <https://en.wikipedia.org/wiki/Interpreter_%28computing%29>`_,
`dynamic programming language <https://en.wikipedia.org/wiki/Dynamic_programming_language>`_.

*Python* was conceived in the late 1980s,and its implementation was started in
December 1989 by `Guido van Rossum <https://en.wikipedia.org/wiki/Guido_van_Rossum>`_
at CWI in the Netherlands as a successor to the `ABC language <https://en.wikipedia.org/wiki/ABC_%28programming_language%29>`_
(itself inspired by SETL).

Van Rossum is Python's principal author, and his continuing central role in deciding
the direction of Python is reflected in the title given to him by the Python community.

*Python* has a large `standard library <https://en.wikipedia.org/wiki/Standard_library>`_,
commonly cited as one of Python's greatest strengths, providing tools suited to many tasks.

*Python* is intended to be a highly readable language.

*Python* uses `whitespace <https://en.wikipedia.org/wiki/Whitespace_character>`_
indentation, rather than `curly braces <https://en.wikipedia.org/wiki/Curly_bracket_programming_language>`_
or keywords, to delimit `blocks <https://en.wikipedia.org/wiki/Block_%28programming%29>`_ ;
this feature is also termed the off-side rule. An increase in indentation comes
after certain statements; a decrease in indentation signifies the end of the current block.


Windows
-------

First, you need to download Python for Windows from the official Website
`<https://www.python.org/ftp/python/3.5.1/python-3.5.1-amd64.exe>`_.

The Windows version is provided as an executable installer (**.exe** file).
To install it manually, just double-click the file.
It's important to remember the path (the directory) where you installed Python.
It'll be needed later.

By design, Python installs to a directory with the version number embedded,
e.g. Python version 3.5 will install at ``C:\Python35\``,
so that you can have multiple versions of Python on the same system without
conflicts.


MacOS
-----

Homebrew (preferred)
^^^^^^^^^^^^^^^^^^^^

First, you need to install a package manager `Homebrew <http://brew.sh/>`_.

To install Homebrew, open Terminal or your favorite OSX terminal emulator
and run::

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Now, you can install Python 3.5::

    $ brew install python

This will take a minute or more.

Package
^^^^^^^

You need to download Python for MacOS from the official Website
`python-3.5.1-macosx10.6.pkg <https://www.python.org/ftp/python/3.5.1/python-3.5.1-macosx10.6.pkg>`_

After that double-click to open it and than double-click
``python-3.5.1-macosx10.6.pkg`` to run the installer.

For verify that installation was completed successful you should
open *Terminal* application and run the command::

   $ python3 --version

You must see something like this::

    $ python --version
    Python 3.5.1

Linux
-----

It's very likely that you already have Python installed out of the box.
To check if you have installed and see which version of Python you have,
open a console and type the following command::

    $ python3 --version

You must see something like this ``Python 3.5.1``.

You do not need to install or configure anything else to use Python.

Setuptools & Pip
^^^^^^^^^^^^^^^^

You can download, install and uninstall any compliant Python software product
with a single command.
It also enables you to add this network installation capability to your own
Python software with very little work.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later
include *pip* by default. To see if *pip* is installed, open a console and run::

    $ which pip

To install *pip*, follow the official pip
`installation guide <https://pip.pypa.io/en/latest/installing/>`_.

This will automatically install the latest version of setuptools.


Flask
=====


**Virtualenv** is probably what you want to use during development.

Most Linux distributions provide a package for virtualenv. For example,
Ubuntu users can install it with this command::

    $ sudo apt-get install python-virtualenv

If you are using Mac OS, then you can install virtualenv using easy_install::

    $ sudo easy_install virtualenv

If you are using Microsoft Windows or any operating system that does not
provide an official virtualenv package, then you have a slightly more
complicated install procedure.

After ``virtualenv`` has been installed, simply run the console and create your
own environment.

Usually in such cases, I create the ``project folder``, and in it - a  ``venv``
folder within::

    $ mkdir myproject

    $ cd myproject

    $ virtualenv venv
    New python executable in venv/bin/python
    Installing distribute............done.

You have to activate the corresponding environment. On MacOS and Linux, do
the following::

    $ source venv/bin/activate

If you are a Windows user, the following command is for you::

    $ venv\scripts\activate

Either way, you should now be using your virtualenv.

Now you can just enter the following command to get Flask activated in your
virtualenv::

    $ pip install Flask

A few seconds later and you are good to go.


Code editors
============

Now is time to write your first line of code, so it's time to download a code
editor.

There are a lot of different editors and it largely boils down to personal
preference.

Most Python programmers use complex but extremely powerful IDEs (Integrated
Development Environments),such as PyCharm.


Atom
----

**Atom** is a cross-platform code editor created by developers for developers.

It is open source, and much like WordPress, Atom users can submit packages and
themes for the software.

It looks pretty and you can change the appearance by installing themes. 

It comes with built-in package manager to extend it, smart autocompletion,
file system browser, multiple panes, find and replace.

You may download from the official web-site `Atom <https://atom.io/>`_

.. image:: image/atom.png

Sublime Text 3
--------------

**Sublime Text** is a cross-platform code editor for Mac, Windows, and Linux.

It comes with all the features you would expect from a powerful code editor and
then some more.

It looks beautiful and you can tweak the appearance to make it more comfortable
for you.

``Sublime Text`` comes with advanced code editor features which allow you to
autofill, autocomplete, reference function in a file, multiple selection,
split editing, and many more.

You may download from the official web-site `Sublime Text <https://www.sublimetext.com/>`_

.. image:: image/sublimetext.png

PyCharm
-------

**PyCharm** editor is a powerful tool for creating and modifying source code.

``PyCharm`` is designed by programmers, for programmers. It provides code analysis,
a graphical debugger, an integrated unit tester, integration with version control
systems (VCSes), and supports web development with Django. 

``PyCharm`` is developed by the Czech company JetBrains.

``PyCharm`` is an Integrated Development Environment (IDE) used for programming 
in Python.

You may download from the official web-site `Pycharm <https://www.jetbrains.com/pycharm/download/>`_

.. image:: image/pycharm.jpg


Why are we installing a code editor?
------------------------------------

You might be wondering why we are installing this special code editor software, 
rather than using something like Word or Notepad.

The first is that code needs to be plain text, and the problem with programs like
Word and Textedit is that they don't actually produce plain text, they produce 
rich text (with fonts and formatting), using custom formats like RTF (Rich Text Format).

The second reason is that code editors are specialised for editing code, so they
can provide helpful features like highlighting code with colour according to its
meaning, or automatically closing quotes for you.
