from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from cafe_form import CafeForm
from data_manager import CSVData
import os

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = os.environ["APP_SECRET_KEY"]

cafe_data = CSVData()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    cafes = cafe_data.get_data()
    form = CafeForm()
    return render_template('cafes.html', cafes=cafes, form=form)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_data.add_data(form)
        return redirect('/cafes')
    return render_template("add.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)

