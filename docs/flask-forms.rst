===========
Flask forms
===========

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


.. _WTForms: http://wtforms.readthedocs.org/en/latest/
.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/