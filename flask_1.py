from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the Main Page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Teja"))

if __name__ == "__main__":
    app.run()