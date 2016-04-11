======
Deploy
======

.. note::

    Based on tutorial `Django Girls <http://tutorial.djangogirls.org/en/>`_
    licensed under `CC-BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_:

Until now, your website was only available on your computer.
Now you will learn how to deploy it! Deploying is the process of publishing
your application on the Internet so people can finally go and see your app.

As you learned, a website has to be located on a server.
There are a lot of server providers available on the internet.
We will use one that has a relatively simple deployment process:
Heroku. Heroku is free for small applications that don't have too many
visitors so it'll definitely be enough for you now.

We will be following this tutorial:
https://devcenter.heroku.com/articles/getting-started-with-python,
but we pasted it here so it's easier for you.

requirements.txt
================

If you didn't create one before, we need to create a requirements.txt
file to tell Heroku what Python packages need to be installed on our server.

But first, Heroku needs us to install a few new packages.
Go to your console with virtualenv activated and type this::

    pip install gunicorn

After the installation is finished run this command::

    pip freeze > requirements.txt

Open this file and add the following line at the bottom::

    psycopg2==2.6.1

Procfile
========

Another thing Heroku wants is a Procfile.
This tells Heroku which commands to run in order to start our website.
Open up your code editor, create a file called Procfile in **FIXME: app**
directory and add this line::

    web: gunicorn app

This line means that we're going to be deploying a web application,
and we'll do that by running the command ``gunicorn app``
(gunicorn is a program that's like a more powerful version of Flask's
development server).

Then save it. Done!

The runtime.txt file
====================

We also need to tell Heroku which Python version we want to use.
This is done by creating a runtime.txt in the app directory
using your editor's "new file" command, and putting the following text
(and nothing else!) inside::

    python-3.5.1

Configuration
=============

Because Heroku wants to use Postgres while we use SQLite for example,
it wants us to use different settings from the ones we use on our locally
(on our computer).

Heroku passes database configuration to application
using environment variables. Update your ``app.py`` the following way:

.. code-block:: python

    import os

    # ...

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///todo.db')


Heroku account
--------------

You need to install your Heroku toolbelt which you can find here
(you can skip the installation if you've already installed it during setup):
https://toolbelt.heroku.com/

After restarting your command prompt, don't forget to go to your
``todoapp`` folder again and activate your ``virtualenv``!
(Hint: Check the Django installation chapter)

Then authenticate your Heroku account on your computer by running
this command::

    $ heroku login

In case you don't have an SSH key this command will automatically
create one. SSH keys are required to push code to the Heroku.

Git repository
--------------

Heroku uses git for its deployments. First you need to create a local
repository, if you haven't done this already::

    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com
    $ git init

Create the file named ``.gitignore`` in your application directory and
add add the following lines to that file::

    *.pyc
    __pycache__
    *.db
    venv

And commit your changes::

    $ git status
    $ git add -A .
    $ git commit -m "Commit files for Heroku"

Create Heroku application
=========================

To create a Heroku application run::

    $ heroku create

Heroku will pick an unused name for you
(probably something like ``desolate-lowlands-28090``

If you ever feel like changing the name of your Heroku application,
you can do so at any time with this command
(replace ``the-new-name`` with the new name you want to use)::

    $ heroku apps:rename the-new-name

Enable PostgreSQL
=================

::

    $ heroku addons:create heroku-postgresql:hobby-dev

Deploy to Heroku!
=================

That was a lot of configuration and installing, right?
But you only need to do that once! Now you can deploy!

When you ran heroku create, it automatically added the Heroku
remote for our app to our repository.
Now we can do a simple git push to deploy our application::

    $ git push heroku master

Visit your application
======================

If you don't know the name of your application simply run::

    $ heroku apps:info

Open your application in the browser via URL like
``https://<appname>.herokuapp.com/``, and at the moment you will probably
see an error page.

The error you saw was because we when we deployed to Heroku, we created
a new database and it's empty. We need to run the ``create_all()``,
just like we did on our local server.

This time, it comes via a special command-line on our own computer,
``heroku run``::

    $ heroku run python

It will open python in the interactive mode on the remote side, so you can
execute::

    >>> from app import db
    >>> db.create_all()

Now restart your application::

    $ heroku restart

Refresh it in your browser, and there you go!
You now know how to deploy your application in the Internet.
