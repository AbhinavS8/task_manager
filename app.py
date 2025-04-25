from flask import Flask,url_for,redirect,render_template,request
from forms import TaskForm
from models import db,Task
from datetime import datetime,timezone
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abhi@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# @app.route("/home")
# def index():
#     return render_template("index.html")

@app.route("/login")
def login():
    return "<p>login page</p>"

@app.route("/tasks/schedule")
def schedule():
    pass

@app.route("/tasks/")
def list_tasks():
    overdue_tasks = Task.query.order_by(Task.due_time).filter(Task.due_time < datetime.now()).all()
    normal_tasks = Task.query.order_by(Task.due_time).filter(Task.completed == False).filter(Task.due_time < datetime.now()).all()
    return render_template('task_list.html', tasks=normal_tasks,o_tasks=overdue_tasks)

@app.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            task_name=form.task_name.data,
            task_category=form.task_category.data,
            start_time=form.start_time.data,
            due_time=form.due_time.data,
            description=form.task_description.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task_list'))
    return render_template('create_task.html', form=form)

@app.route("/tasks/<int:id>")
def task_detail(id):
    task = Task.query.get_or_404(id)
    return render_template('task_detail.html', task=task)

@app.route("/tasks/completed")
def completed_tasks():
    return "<p>Completed tasks page</p>"


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/tasks/<int:id>/complete', methods=['POST'])
def complete_task(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('task_detail', id=id))

# @app.route('/post/<int:id>')
# def post(id):
#     # show the post with the given id, the id is an integer
#     return 'Post '+str(id)

# # @app.route('/projects/')
# # def projects():
# #     return 'The project page'

# @app.route('/projects')
# def projects():
#     return 'The skbi page'

# @app.route("/top_post")
# def show_top_post():
#     return redirect(url_for("post",id=1)) #instead of redirect(/post/1)