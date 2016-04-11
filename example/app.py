import os

from wtforms import Form, BooleanField, TextAreaField
from wtforms import validators

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

application = app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///todo.db')
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    is_done = db.Column(db.Boolean)

    def __repr__(self):
        return '<Task {0}, {1!r}>'.format(self.id, self.content)


class TaskForm(Form):
    content = TextAreaField('Task', [validators.DataRequired()])
    is_done = BooleanField('Done')


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/task/new', methods=['GET', 'POST'])
def create_task():
    form = TaskForm(request.form)
    if request.method == 'POST' and form.validate():
        task = Task(content=form.content.data, is_done=form.is_done.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('task_edit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
