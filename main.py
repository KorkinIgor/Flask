++from flask import Flask, render_template, request+
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)  #указывает имя приложения(оно берется из названия скрипта)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'  #Создаем базу данных
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #2 входных параметра, один отвечает за тип данных, второй за уникальность значений
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

@app.route("/")  #Декоратор - принимает на вход функцию
def index():
    return render_template("index.html")  #возращаем страницу

@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = Post(title=title, text=text)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("create.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":  #если приложения запущено с этого файла
    app.run(debug=True)  #debug=True позволяет не перезапускать сервер



