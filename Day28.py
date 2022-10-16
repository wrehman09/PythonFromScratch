#post request with flask and html form 


from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

@app.route("/")
def hello_world():
     return render_template("form.html")

@app.route("/fl")
def home():
    return render_template("Flask_JinJa.html",name="Wasi Rehman")


@app.route("/senddata", methods=['POST'])
def senddata():
    print(request.form["uname"])
    print(request.form["pass"])
    return "Success"
         

app.run()