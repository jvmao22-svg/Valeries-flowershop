from flask import Flask, render_template, request

app = Flask(__name__)

roses = ["pink", "red", "white", "orange", "yellow", "green", "blue", "purple"]
fillers = ["daisies", "delphinium", "bells_of_ireland"]
others = ["lilies", "tulips", "carnations", "sunflowers"]
wrappings = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
gifts = ["teddybear", "bunny", "chocolate"]


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
