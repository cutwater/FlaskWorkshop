============
Installation
============

Python
======

Windows
-------

.. todo:: TBD
First, you need to download Python for Windows from the official Website .. _a link: https://www.python.org/downloads/release/python-351/
The Windows version is provided as an MSI package(***.msi** file). To install it manually, just double-click the file.
The MSI package format allows Windows administrators to automate installation with their standard tools.
It's important to remember the path(the directory) where you installed Python. It'll be needed later.
By design, Python installs to a directory with the version number embedded, e.g. Python version 3.5 will install at *C:\Python35\*,
so that you can have multiple versions of Python on the same system without conflicts.


MacOS
-----

.. todo:: TBD
You need to download Python for MacOS from the official Website .. _a link: https://www.python.org/downloads/release/python-351/
After that double-click to open it and than double-click *Python.mpkg* to run the installer.
For verify that installation was completed successful you shoul open *Terminal* application and run the command:``python3 --version``
You must see something like this *Python 3.5.1*.

Another way to install Python. First, you need to install a package manager **Homebrew**.
To install *Homebrew*, open Terminal or your favorite OSX terminal emulator and run
``$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``
Now, we can install Python 3.5:
``$ brew install python``
This will take a minute or more.


Linux
-----

.. todo:: TBD

It's very likely that you already have Python installed out of the box. To check if you have installed
and see which version of Python you have, open a console and type the following command:
``python3 --version``
You must see something like this *Python 3.5.1*.

You do not need to install or configure anything else to use Python.

:sup:Setuptools:sup:&:sup:Pip

You can download, install and uninstall any compliant Python software product with a single command.

It also enables you to add this network installation capability to your own Python software with very little work.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include *pip* by default.
To see if *pip* is installed, open a console and run ``$ command -v pip``

To install *pip*, follow the official pip installation guide .. _a link: https://pip.pypa.io/en/latest/installing/
This will automatically install the latest version of setuptools.


Flask
=====

.. todo:: TBD
**Virtualenv** is probably what you want to use during development.
Most Linux distributions provide a package for virtualenv. For example, Ubuntu users can install it with this command:
``$ sudo apt-get install python-virtualenv``
If you are using Mac OS, then you can install virtualenv using easy_install:
``$ sudo easy_install virtualenv``
If you are using Microsoft Windows or any operating system that does not provide an official virtualenv package, then
you have a slightly more complicated install procedure.

After *virtualenv* has been installed, simply run the console and create your own environment. 
Usually in such cases, I create the *project folder*, and in it - a  *venv* folder within:
``$ mkdir myproject``
``$ cd myproject``
``$ virtualenv venv``
*New python executable in venv/bin/python*
*Installing distribute............done.*

You have to activate the corresponding environment. On MacOS and Linux, do the following:
``$ source venv/bin/activate``
If you are a Windows user, the following command is for you:
``$ venv\scripts\activate``

Either way, you should now be using your virtualenv.

Now you can just enter the following command to get Flask activated in your virtualenv:
``$ pip install Flask``
A few seconds later and you are good to go.


Code editors
============

.. todo:: TBD

Atom
----

.. todo:: TBD

Sublime Text 3
--------------

.. todo:: TBD

PyCharm
-------

.. todo:: TBD
