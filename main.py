from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    title = "Home"
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]
    return render_template(
                           "index.html",
                           title=title,
                           current_year=current_year,
                           cities=cities
    )


@app.route("/about-me")
def about():
    title = "About"
    return render_template("about.html", title=title)


if __name__ == '__main__':
    app.run()