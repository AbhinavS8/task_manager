from flask import Flask,url_for,redirect,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",name = "world")

@app.route('/post/<int:id>')
def post(id):
    # show the post with the given id, the id is an integer
    return 'Post '+str(id)

# @app.route('/projects/')
# def projects():
#     return 'The project page'

@app.route('/projects')
def projects():
    return 'The skbi page'

@app.route("/top_post")
def show_top_post():
    return redirect(url_for("post",id=1)) #instead of redirect(/post/1)