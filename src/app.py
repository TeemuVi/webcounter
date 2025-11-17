from flask import Flask, redirect, request, render_template
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def set_number():
    number = int(request.form.get("value",0))
    cnt.value = number
    return redirect("/")
    
@app.route("/reset", methods=["POST"])
def reset():
    cnt.value = 0
    return redirect("/")
    
@app.route("/reset", methods=["POST"])
def test_reset():
    cnt.value = 0
    return "Reset"