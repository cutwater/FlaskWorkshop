===========
Flask forms
===========

.. note::

    Based on tutorial `Django Girls <http://tutorial.djangogirls.org/en/>`_
    licensed under `CC-BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_:

The next thing we want to do on our website is create a nice way to
add and edit tasks. With forms we will have absolute power over our
interface - we can do almost anything we can imagine!

Flask doesn't have any helpers for forms. It doesn't mean that you can't
work with html forms in Flask, but when you have to work with form data
submitted by a browser view code quickly becomes very hard to read.

There are libraries out there designed to make this process easier to manage.
One of them is `WTForms`_ which we will handle here.
If you find yourself in the situation of having many forms,
you might want to give it a try.

The `Flask-WTF`_ extension expands on this pattern and adds a few handful
little helpers that make working with forms and Flask more fun.

So first let's install Flask-WTF extension::

    pip install Flask-WTF

When you are working with WTForms you have to define your forms
as classes first:

.. code-block:: python

    from wtforms import Form, BooleanField, TextAreaField
    from wtforms import validators

    # ...

    class TaskForm(Form):
        content = TextAreaField('Task', [validators.DataRequired()])
        is_done = BooleanField('Done')

Now let's create a new view:

.. code-block:: python

    from flask import request, redirect, url_for

    # ...

    @app.route('/task/new', methods=['GET', 'POST'])
    def create_task():
        form = TaskForm(request.form)
        if request.method == 'POST' and form.validate():
            task = Task(content=form.content.data, is_done=form.is_done.data)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('task_edit.html', form=form)

.. todo:: Describe function

And template ``task_edit.html``:

.. code-block:: html+jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TODO App</title>
    </head>
    <body>
        <h1>New task</h1>
        <form method="POST" action="">
            <ul>
            {% for field, errors in form.errors.items() %}
                {% for error in errors %}
                <li>{{ form[field].label.text }}: {{ error }}</li>
                {% endfor %}
            {% endfor %}
            </ul>
            <div>{{ form.content.label }} {{ form.content }}</div>
            <div>{{ form.is_done.label }} {{ form.is_done }}</div>
            <input type="submit" value="Create" />
        </form>
    </body>
    </html>

Now just add:

.. code-block:: html+jinja

    <a href="{{ url_for('create_task') }}">New task</a>

to your ``index.html``.


Organizing templates
====================

You may noticed that we’ve just duplicated a lot of HTML.

Our template examples so far have been tiny HTML snippets,
but in the real world, you’ll be using Flask’s template system
to create entire HTML pages. This leads to a common Web development problem:
across a Web site, how does one reduce the duplication and redundancy
of common page areas, such as sitewide navigation?

Imagine if we had a more typical site, including a navigation bar,
a few style sheets, perhaps some JavaScript – we’d end up putting all
sorts of redundant HTML into each template.

In essence, template inheritance lets you build a base "skeleton" template
that contains all the common parts of your site and defines "blocks"
that child templates can override.

Flask’s template inheritance system solves these problems.

The first step is to define a base template – a skeleton of your page that
child templates will later fill in. Here’s a base template for our
ongoing example:

Create a new template file and call it ``layout.html``.

.. code-block:: html+jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TODO App{% block title %}{% endblock %}</title>
    </head>
    <body>
        <header>
        {% block header %}
            <h1><a href="">TODO App</a></h1>
        {% endblock %}
        </header>

        {% block body %}
        {% endblock %}
    </body>
    </html>

This template defines a simple HTML skeleton document that we’ll use for
all the pages on the site. It’s the job of child templates to override,
or add to, or leave alone the contents of the blocks.

Now that we have this base template, we can modify our existing
``index.html`` template to use it:

.. code-block:: html+jinja

    {% extends 'layout.html' %}

    {% block body %}
        <div class="task-list">
            {% for task in tasks %}
            <div class="task">
                <input type="checkbox" {% if task.is_done %}checked{% endif %}>
                {{ task.content }}
            </div>
            {% endfor %}
        </div>
        <a href="{{ url_for('create_task') }}">New task</a>
    {% endblock %}

And now let's do the same for our ``task_edit.html`` template:

.. code-block:: html+jinja

    {% extends 'layout.html' %}

    {% block title %} : New task {% endblock %}

    {% block body %}
        <h1>New task</h1>
        <form method="POST" action="">
            <ul>
            {% for field, errors in form.errors.items() %}
                {% for error in errors %}
                <li>{{ form[field].label.text }}: {{ error }}</li>
                {% endfor %}
            {% endfor %}
            </ul>
            <div>{{ form.content.label }} {{ form.content }}</div>
            <div>{{ form.is_done.label }} {{ form.is_done }}</div>
            <input type="submit" value="Create" />
        </form>
    {% endblock %}

Isn’t this beautiful? Each template contains only the code that’s unique
to that template. No redundancy needed.
If you need to make a site-wide design change, just make the change
to ``layout.html``, and all of the other templates will immediately
reflect the change.

.. _WTForms: http://wtforms.readthedocs.org/en/latest/
.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/