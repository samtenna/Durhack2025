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

@app.route("/register")
def register():
    return render_template("register.html")

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
        "Desc": "Home of tartan, haggis and the Loch Ness Monster, Scotland has a rich history not only in the cobbled streets of Edinburgh but also in the gorgeous country, where in the winter you may catch a glimpse of the northern lights."
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
    },
    6: {
        "City": "Se",
        "Desc": "Beautiful City"
    },
    7: {
        "City": "East-Anglia",
        "Desc": "Beautiful City"
    },
    8: {
        "City": "West-midlands",
        "Desc": "Beautiful City"
    },
    9: {
        "City": "East-midlands",
        "Desc": "Beautiful City"
    },
    10: {
        "City": "Nw",
        "Desc": "Beautiful City"
    },
    11: {
        "City": "Ne",
        "Desc": "Beautiful City"
    },
    12: {
        "City": "",
        "Desc": "Beautiful City"
    }

}


# TODO change this line of code
current = []

@app.route("/pins/<int:pin_id>", methods=['GET'])
def find_pin(pin_id):
    global current

    if pin_id in current:
        current.remove(pin_id)
        return make_response(
            ""
        )
    else:
        current.append(pin_id)
        response = f""" 
            <div class="bg-white">
                <p class="text-xl text-black">{pins[pin_id]["City"]}</p>
                <p class="text-sm text-black">{pins[pin_id]["Desc"]}</p>
            </div>

        """
        return make_response(
            response,
            push_url=False,
            trigger={"event1": "A message", "event2": "Another message"},
    )




app.run(debug=True)