=====================
Introduction to Flask
=====================

`Flask`_ is a microframework for building web applications using Python
programming language written by Armin Ronacher. For Flask microframework
means that it aims to keep the core simple but extensible.
Flask doesn't make decisions for you, such as what database to use.

By default, Flask does not include a database abstraction layer,
form validation or anything else where different libraries already
exist that can handle that.

Instead, Flask supports extensions to add such functionality
to your application as if it was implemented in Flask itself.
Numerous extensions provide database integration, form validation,
upload handling, various open authentication technologies, and more.

The most convenient way to install Flask is to use a virtual environment (:ref:`install-virtualenv`).
A virtual environment is a private copy of the Python interpreter onto which
you can install packages privately without installed in your system.


Why do you need a framework?
----------------------------

Web frameworks encapsulate what developers have learned over the past twenty years
while programming sites and applications for the web. Frameworks make it easier
to reuse code for common HTTP operations and to structure projects so other
developers with knowledge of the framework can quickly build and maintain
the application.

To understand what Flask actually is for, we need to take a closer look at the
servers. The first thing is that the server needs to know that you want it to
serve you a web-page.

Imagine a mailbox (port) which is monitored for incoming letters (requests).
This is done by a web server. The web server reads the letter, and sends a response
with a web-page. But when you want to send something, you need to have some content.
And Flask is something that helps you create the content.

Why is Flask a good web framework choice?
-----------------------------------------

:ref:`install-virtualenv` is considered more `Pythonic <http://blog.startifact.com/posts/older/what-is-pythonic.html>`_
than Django because Flask web application code is in most cases more explicit.
*Flask* is easy to get started with as a beginner because there is little
boilerplate code for getting a simple app up and running.

For example, here's a valid ``"hello world"`` web application with Flask:

.. code-block:: python
   :emphasize-lines: 2,9

   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello World!'

   if __name__ == '__main__':
       app.run()


.. _Flask: http://flask.pocoo.org/
