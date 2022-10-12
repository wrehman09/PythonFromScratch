#beginner web development with FLASK 
  
from flask import Flask
from flask import render_template

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, Wasi !</p>"

@app.route("/wasi")
def hello_wasi():
    return "<p>Hello, rehman !</p>"



@app.route("/name/<name>")
def hello_name(name):
    return f"<p>Hello, {name} !</p>"

# to render template it should be in template folder 
@app.route("/website")
def website():
    return render_template("Website.html")



#to run command  C:/Users/wasi_/AppData/Local/Programs/Python/Python39/python.exe -m flask --app Day25 run
# or using app.run 

app.run()