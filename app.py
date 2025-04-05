from flask import Flask,url_for,redirect,render_template,request
from models import db,Task
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abhi@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return "<p>login page</p>"

@app.route("/tasks/schedule")
def schedule():
    pass

@app.route("/tasks")
def list_tasks():
    pass

@app.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_category = request.form['task_category']
        start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M')
        due_time = datetime.strptime(request.form['due_time'], '%Y-%m-%dT%H:%M')

        task = Task(
            task_name=task_name,
            task_category=task_category,
            start_time=start_time,
            due_time=due_time
        )

        db.session.add(task)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("create_task.html")

@app.route("/tasks/<int:id>")
def task_detail(id):
    pass

@app.route("/tasks/completed")
def completed_tasks():
    return "<p>Completed tasks page</p>"


# @app.route("/")
# def hello_world():
#     return render_template("index",name = "hello world")

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