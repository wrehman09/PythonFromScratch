#python  dunamic html pages   jinja 

from unicodedata import name
from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Wasi !</p>"

@app.route("/fl")
def home():
    return render_template("Flask_JinJa.html",name="Wasi Rehman")

app.run()