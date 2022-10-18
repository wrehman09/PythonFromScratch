from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

all_books = []
db = sqlite3.connect("books-collection.db", check_same_thread=False)
cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


@app.route('/')
def home():
    global all_books
    cursor.execute("SELECT * FROM books")

    rows = cursor.fetchall()
    print(rows)
    #all_books = db.session.query(Book).all()
    return render_template("index.html",all_books=all_books)


@app.route("/add")
def add():
     return render_template("add.html")


@app.route("/senddata", methods=['POST'])
def senddata():
    
    global all_books
    all_books.append({
        "title": request.form["title"],
        "author": request.form["author"],
        "rating": request.form["rating"],
    })
    ins=f"INSERT INTO books VALUES(675, '{request.form['title']}', '{request.form['author']}', '{request.form['rating']}')"
    print(ins)



    cursor.execute(ins)
    db.commit()



    return render_template("index.html",all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

