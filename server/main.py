from flask import Flask, render_template, jsonify
from dataclasses import dataclass
from flask_htmx import HTMX, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
htmx = HTMX(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

@dataclass
class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Region {self.name}>"

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/regions")
def regions_list():
    regions = db.session.execute(db.select(Region)).scalars().all()
    regions = [{"name": region.name, "description": region.description} for region in regions]
    return jsonify(regions)

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
        "City": "ni",
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
                <p class="text-xl text-black">{pins[pin_id]["Desc"]}</p>
            </div>

        """
        return make_response(
            response,
            push_url=False,
            trigger={"event1": "A message", "event2": "Another message"},
    )




app.run(debug=True)