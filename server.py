from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("all-cupcakes.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

@app.route("/cupcake_individual")
def individual_cupcake():
    return render_template("individual.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")




