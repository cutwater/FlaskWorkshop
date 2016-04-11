============
Flask models
============

.. note::

    Based on tutorial `Django Girls <http://tutorial.djangogirls.org/en/>`_
    licensed under `CC-BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_:


What we want to create now is something that will store all the tasks in our
application. But to be able to do that we need to talk a little bit about things
called objects.

A model in Flask is a special kind of object - it is saved in the database.
A database is a collection of data. This is a place in which you will store
information about users, tasks, your blog posts, etc.

We will be using a SQLite database to store our data.
It'll be enough for us right now.

You can think of a model in the database as a spreadsheet with columns (fields)
and rows (data).

Installing Flask-SQLAlchemy
===========================

Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy
to your application. It requires SQLAlchemy 0.6 or higher.
It aims to simplify using SQLAlchemy with Flask by providing useful
defaults and extra helpers that make it easier to accomplish common tasks.

To install ``Flask-SQLAlchemy`` just type::

    pip install Flask-SQLALchemy


Creating a model
================

For the common case of having one Flask application all you have to do
is to create your Flask application, load the configuration of choice
and then create the SQLAlchemy object by passing it the application.

Once created, that object then contains all the functions and helpers
from both ``sqlalchemy`` and ``sqlalchemy.orm``. Furthermore it provides a class
called Model that is a declarative base which can be used to declare models::


    from flask import Flask
    from flask import render_template
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    db = SQLAlchemy(app)


    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.Text)
        created_at = db.Column(db.DateTime)
        is_done = db.Column(db.Boolean)

        def __repr__(self):
            return '<Task {0}, {1!r}>'.format(self.id, self.content)

    ...

To create the initial database, just import the db object from an interactive
Python shell and run the ``SQLAlchemy.create_all()`` method to create the
tables and database::

    >>> from app import db
    >>> db.create_all()

Boom, and there is your database. You can find a new file ``todo.db`` in
the same directory where your ``app.py`` is located.

Now to create some tasks::

    >>> from app import Task
    >>> task1 = Task(content='Write static template with items.')
    >>> task2 = Task(content='Display items from the database.')

But they are not yet in the database, so let’s make sure they are::

    >>> db.session.add(task1)
    >>> db.session.add(task2)
    >>> db.session.commit()

Accessing the data in database is easy as a pie::

    >>> tasks = Task.query.all()
    >>> print(tasks)
    [<Task 1, 'Write static template with items.'>, <Task 2, 'Display items from the database.'>]

So you have already inserted some tasks into your database. If everything went
fine, you should find file ``todo.db`` in your project directory.

Now let's make our application displaying these records. For this you will
need to make a query and get all records from the database in your ``index``
view:

#. You need to make a query to get all records from the database as
   we did this before::

    tasks = Task.query.all()

#. And pass ``tasks`` list to the template, so template will know about
   tasks variable and you will be able to use it in your ``index.html``::

    return render_template('index.html', tasks=tasks)

A complete example looks like:

.. code-block:: python

    # ...

    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    # ...

Now you can update template to generate items dynamically:

.. code-block:: html+jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TODO App</title>
    </head>
    <body>
        <h1><a href="">TODO App</a></h1>
        <div class="task-list">
            {% for task in tasks %}
            <div class="task">
                <input type="checkbox" {% if task.is_done %}checked{% endif %}>
                {{ task.content }}
            </div>
            {% endfor %}
        </div>
    </body>
    </html>


Congratulations! Now you have an application that stores data in the database.
Easy, isn't it? But wait, we can display the data, but cannot edit it.
And doing it manually as we did using Python's interactive is the best way
to do it.

So next we will show you how to add new tasks and edit existing tasks in your
web application using forms.