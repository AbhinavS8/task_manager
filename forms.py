from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime, timezone, timedelta

class TaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    task_category = StringField('Task Category', validators=[DataRequired()])
    start_time = DateTimeLocalField(
        'Start Time',
        format='%Y-%m-%dT%H:%M',
        default=datetime.now(timezone.utc)+timedelta(hours=5,minutes=30),
        validators=[DataRequired()]
    )
    due_time = DateTimeLocalField(
        'Due Time',
        format='%Y-%m-%dT%H:%M',
        default=datetime.now(timezone.utc)+timedelta(hours=5,minutes=30),
        validators=[DataRequired()]
    )
    task_description = TextAreaField('Task Description', validators=[DataRequired()])
    submit = SubmitField('Create Task')
