from flask import Flask, render_template, request
from utils import (
    rashis,
    nakshatras,
    get_sublord,
    get_nakshatra_timings,
    get_sublords_timings,
)
import json, requests
import datetime
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html", rashis=rashis, nakshatras=nakshatras)
    else:
        rashi = request.form.get("rashi")
        nakshatra = request.form.get("nakshatra")
        date_str = request.form.get("datetime")

        # Parsing the date string
        date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
        nakshatra_timings = json.loads(get_nakshatra_timings(date))

        final = None
        output = "Select Correct Combination"

        try:
            output = get_sublord(rashi=rashi, nakshatra=nakshatra)
            final = get_sublords_timings(
                datetime.datetime.strptime(
                    nakshatra_timings["starts_at"], "%Y-%m-%d %H:%M:%S"
                ),
                output,
            )
        except Exception as e:
            print("error in final", e)

        return render_template(
            "index.html",
            output=output,
            rashis=rashis,
            nakshatras=nakshatras,
            nakshatra_timings=nakshatra_timings,
            final=final,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
