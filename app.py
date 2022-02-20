from flask import Flask, render_template, request, session, jsonify
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "items" not in session:
        session["items"] = []
    return render_template("index.html", items=session["items"])

@app.route("/get", methods=["GET"])
def get():
    items = session["items"]
    items.append(request.args.get("todo"))
    return jsonify(items)