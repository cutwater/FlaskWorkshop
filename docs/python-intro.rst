======================
Introduction to Python
======================

What is Python?
===============

Python is a very popular programming language that can be used for
creating websites, games, scientific software, graphics, and much, much more.

Python is an easy to learn, powerful programming language.
It has efficient high-level data structures and a simple but effective
approach to object-oriented programming.

Python's elegant syntax and dynamic typing, together with its
interpreted nature, make it an ideal language for scripting
and rapid application development in many areas on most platforms.

Python originated in the late 1980s and its main goal is to be readable
by human beings (not only machines).
This is why it looks much simpler than other programming languages.
This makes it easy to learn, but don't worry, Python is also really powerful!

Using the Python interpreter
----------------------------

The Python interpreter is usually installed as ``/usr/local/bin/python3.5``
on those machines where it is available; putting ``/usr/local/bin``
in your Unix shell’s search path makes it possible to start
it by typing the command::

    python3.5

On Windows machines, the Python installation is usually placed
in ``C:\Python35``, though you can change this when you're running
the installer.

Typing an end-of-file character (``Control-D`` on Unix,
``Control-Z`` on Windows) at the primary prompt causes the interpreter
to exit with a zero exit status. If that doesn’t work, you can exit the
interpreter by typing the following command: ``quit()``.

Interactive mode
----------------

When commands are read from a tty, the interpreter is said to be in
interactive mode. In this mode it prompts for the next command with
the primary prompt, usually three greater-than signs (``>>>``);
for continuation lines it prompts with the secondary prompt,
by default three dots (``...``).
The interpreter prints a welcome message stating its version number
and a copyright notice before printing the first prompt::

    $ python3.5
    Python 3.5 (default, Sep 16 2015, 09:25:04)
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Continuation lines are needed when entering a multi-line construct.
As an example, take a look at this if statement::

    >>> the_world_is_flat = True
    >>> if the_world_is_flat:
    ...     print("Be careful not to fall off!")
    ...
    Be careful not to fall off!

Data types
==========

What is a data type?
--------------------

In computer science and computer programming, a **data type** or simply **type**
is a classification identifying one of various types of data, such as **real**,
**integer** or **boolean**, that determines the possible values for that type;
the operations that can be done on values of that type;
the meaning of the data; and the way values of that type can be stored.

