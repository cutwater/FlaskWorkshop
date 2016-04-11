===============
Flask templates
===============

.. note::

    Based on tutorial `Django Girls <http://tutorial.djangogirls.org/en/>`_
    licensed under `CC-BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_:

A template is a file that we can re-use to present different information
in a consistent format - for example, you could use a template to help
you write a letter, because although each letter might contain a different
message and be addressed to a different person, they will share
the same format.

A Flask template's format is described in a language called HTML.

What's HTML?
============

HTML is a simple code that is interpreted by your web browser - such as Chrome,
Firefox or Safari - to display a web-page for the user.

HTML stands for "HyperText Markup Language". *HyperText* means it's a type of
text that supports hyperlinks between pages. *Markup* means we have taken a
document and marked it up with code to tell something (in this case, a browser)
how to interpret the page. HTML code is built with *tags*, each one starting
with < and ending with >. These tags represent markup *elements*.

Your first template
===================

Creating a template means creating a template file.
Everything is a file, right? You have probably noticed this already.

Templates are saved in ``templates`` directory.

So create directory ``templates`` near your ``app.py`` file.

Now create file ``templates/index.html`` and add the following code to your
template file:

.. code-block:: html

   <html>
       <h1>Hi there!</h1>
       <p>It works!</p>
   </html>

Now we need tell Flask to display this template. Update your ``app.py``:

.. code-block:: python
   :emphasize-lines: 2,9

   from flask import Flask
   from flask import render_template

   app = Flask(__name__)


   @app.route('/')
   def index():
       return render_template('index.html')


   if __name__ == '__main__':
       app.run()

Now run ``app.py`` and see how your website looks now: http://127.0.0.1:5000/


.. image:: image/screenshot/flask-first-template-1.png

It worked! Nice work there :)

* The most basic tag, ``<html>``, is always the beginning of any webpage
  and ``</html>`` is always the end. As you can see, the whole content
  of the website goes between the beginning tag ``<html>`` and closing tag
  ``</html>``.
* ``<p>`` is a tag for paragraph elements; ``</p>`` closes each paragraph.

Head & body
===========

Each HTML page is also divided into two elements: **head** and **body**.

* **head** is an element that contains information about the document that
  is not displayed on the screen.
* **body** is an element that contains everything else that is displayed
  as part of the web page.

We use ``<head>`` to tell the browser about the configuration of the page,
and ``<body>`` to tell it what's actually on the page.

For example, you can put a webpage title element inside the <head>, like this:

.. code-block:: html

   <html>
   <head>
       <title>My First Template</title>
   </head>
   <body>
       <h1>Hi there!</h1>
       <p>It works!</p>
   </body>
   </html>

.. image:: image/screenshot/flask-first-template-2.png

Notice how the browser has understood that "My First template" is the title
of your page? It has interpreted ``<title>My First Template</title>``
and placed the text in the title bar of your browser
(it will also be used for bookmarks and so on).

Probably you have also noticed that each opening tag is matched
by a closing tag, with a /, and that elements are nested
(i.e. you can't close a particular tag until all the ones that were
inside it have been closed too).

It's like putting things into boxes. You have one big box, ``<html></html>``;
inside it there is ``<body></body>``, and that contains still smaller boxes:
``<p></p>``.

You need to follow these rules of closing tags, and of nesting
elements - if you don't, the browser may not be able to interpret
them properly and your page will display incorrectly.

A complete example
==================

The example above was not complete. Many browsers will display this page
in a correct way. This happens because browsers trying to be
tolerant to code mistakes or missing parts. The following example shows
how valid HTML page should look like:

.. code-block:: html
   :emphasize-lines: 1,4

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>My First Template</title>
   </head>
   <body>
       <h1>Hi there!</h1>
       <p>It works!</p>
   </body>
   </html>

Document type
^^^^^^^^^^^^^

The doctype for HTML5 is very simple.
To indicate that your HTML content uses HTML5, simply use::

    <!DOCTYPE html>

Doing so will cause even browsers that don't presently support HTML5
to enter into standards mode, which means that they'll interpret
the long-established parts of HTML in an HTML5-compliant way while
ignoring the new features of HTML5 they don't support.

This is much simpler than the former doctypes, and shorter,
making it easier to remember and reducing the amount of bytes
that must be downloaded.

Character set
^^^^^^^^^^^^^
The first thing done on a page is usually indicating the character
set that is used. In previous versions of HTML, it was done using
a very complex ``<meta>`` element. Now, it is very simple::

   <meta charset="UTF-8">

Place this right after your ``<head>``, as some browsers restart the parsing
of an HTML document if the declared charset is different from what they
had anticipated. Also, if you are not currently using ``UTF-8``, it's
recommended that you switch to it in your Web pages, as it simplifies
character handling in documents using different scripts.

Customizing template
====================

You can now have a little fun and try to customize your template!
Here are a few useful tags for that:

* ``<h1>A heading</h1>`` - for your most important heading
* ``<h2>A sub-heading</h2>`` for a heading at the next level
* ``<h3>A sub-sub-heading</h3>`` ... and so on, up to ``<h6>``
* ``<em>text</em>`` emphasizes your text
* ``<strong>text</strong>`` strongly emphasizes your text
* ``<br />`` goes to another line (you can't put anything inside br)
* ``<a href="http://google.com">link</a>`` creates a link
* ``<ul><li>first item</li><li>second item</li></ul>``
  makes a list, just like this one!
* ``<div></div>`` defines a section of the page


.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My First Template</title>
    </head>
    <body>
        <h1><a href="">TODO App</a></h1>
        <div>
            <input type="checkbox">
            Write static template with items.
        </div>
        <div>
            <input type="checkbox">
            Display items from the database.
        </div>
        <div>
            <input type="checkbox">
            Add items using form.
        </div>
        <div>
            <input type="checkbox" checked>
            Create first Flask application.
        </div>
    </body>
    </html>

We've created three one ``h1`` and four ``div`` sections here.

* The ``h1`` element contains the title of our application.
* Four ``div`` elements contain our tasks with text,
  and a checkbox to mark task as done or not done.

It gives us this effect:

.. image:: image/screenshot/todo-index-1.png

Looks nice. But so far, our template only ever displays exactly the same
information - whereas earlier we were talking about templates as allowing
us to display different information in the same format.

What we really want to do is display real tasks
and that's where we're going next.
