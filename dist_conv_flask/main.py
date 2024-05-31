from flask import Flask, request, render_template

app = Flask(__name__)


def convert_units(conversion_type, org_value):
    if conversion_type == "k2m":
        conv_value = round((org_value * 0.6214), 2)
        old_units, new_units = "kilometers", "miles"
    else:
        conv_value = round((org_value * 1.6090), 2)
        old_units, new_units = "miles", "kilometers"
    return f"{org_value} {old_units} is {conv_value} {new_units}."


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", converted_units="")
    else:
        conversion = request.form["conversionType"]
        units = float(request.form["unitToConvert"])
        answer = convert_units(conversion, units)
        return render_template("index.html", converted_units=answer)


if __name__ == "__main__":
    app.run()
