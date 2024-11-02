from flask import Flask, render_template
from flask_htmx import HTMX, make_response

app = Flask(__name__)
htmx = HTMX(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/hola-mundo")
def hola_mundo():
    body = "Hola Mundo!"
    return make_response(
        body,
        push_url=False,
        trigger={"event1": "A message", "event2": "Another message"},
    )

pins = {
    1 : {
        "City": "London",
        "Desc": "Beautiful City"
    },

    2 : {
        "City": "Yorkshire",
        "Desc": "Beautiful City"
    },

    3: {
        "City": "Scotland",
        "Desc": "Beautiful City"
    },
    4: {
        "City": "Wales",
        "Desc": "Beautiful City"
    },
    5: {
        "City": "Sw",
        "Desc": "Beautiful City"
    }

}


@app.route("/pins/<int:pin_id>", methods=['GET'])
def find_pin(pin_id):

    response = f""" 
        <div class="bg-white">
            <p class="text-xl text-black">{pins[pin_id]["City"]}</p>
            <p class="text-xl text-black">{pins[pin_id]["Desc"]}</p>
        </div>

    """
    return make_response(
        response,
        push_url=False,
        trigger={"event1": "A message", "event2": "Another message"},
    )




app.run(debug=True)