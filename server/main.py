from flask import Flask, render_template
from flask_htmx import HTMX

app = Flask(__name__)
htmx = HTMX(app)

@app.route("/")
def index():
    return render_template("index.html")

from flask_htmx import make_response

@app.route("/hola-mundo")
def hola_mundo():
    body = "Hola Mundo!"
    return make_response(
        body,
        push_url=False,
        trigger={"event1": "A message", "event2": "Another message"},
    )

app.run(debug=True)