============
Flask models
============

What we want to create now is something that will store all the
tasks in our application. But to be able to do that we need to talk a
little bit about things called objects.

A model in Flask is a special kind of object - it is saved in the database.
A database is a collection of data. This is a place in which you will store
information about users, tasks, your blog posts, etc.

We will be using a SQLite database to store our data.
It'll be enough for us right now.

You can think of a model in the database as a spreadsheet
with columns (fields) and rows (data).

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
from both sqlalchemy and sqlalchemy.orm. Furthermore it provides a class
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

    $ python
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
