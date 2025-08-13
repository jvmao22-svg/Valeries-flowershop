from flask import Flask, render_template, request

app = Flask(__name__)

roses = ["Pink", "Red", "White", "Orange", "Yellow", "Green", "Blue", "Purple"]
fillers = ["Daisies", "Delphinium", "Bells_of_ireland"]
others = ["Lilies", "Tulips", "Carnations", "Sunflowers"]
wrappings = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]
gifts = ["Teddybear", "Bunny", "Chocolate"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selections = {
            "rose": request.form["rose"],
            "filler": request.form["filler"],
            "other": request.form["other"],
            "wrapping": request.form["wrapping"],
            "gift": request.form["gift"]
        }
        return render_template("result.html", selections=selections)
    return render_template("index.html", roses=roses, fillers=fillers, others=others, wrappings=wrappings, gifts=gifts)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
