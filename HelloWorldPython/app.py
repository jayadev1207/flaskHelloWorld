from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')   
def rootPage():
  return render_template("index.html")
@app.route('/hello')   
def hello():
  return "Hello World "
 

app.run()