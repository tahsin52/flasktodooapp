from flask import Flask,render_template,redirect,url_for,request,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/User/Desktop/TodoApp/todoo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todoo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/complete/<string:id>")
def completeTodoo(id):
    todo = Todoo.query.filter_by(id=id).first()
    """if todo.complete == True:
        todo.complete = False
    else:
        todo.complete == True """     
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def addTodoo():
    title = request.form.get("title")
    newTodoo = Todoo(title = title,complete = False)
    db.session.add(newTodoo)

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodoo(id):
    todo = Todoo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


class Todoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
