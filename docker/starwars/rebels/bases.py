import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


endpoints = ("alderaan", "endor", "hoth", "coruscant", "yavin4", "dantooine", "corellia", "sullust", "ansion", "bastion", "gralle", "empire")


@app.route("/alderaan")
def alderaan():
    time.sleep(random.random() * 0.2)
    return "ok"


@app.route("/endor")
def endor():
    time.sleep(random.random() * 0.4)
    return "ok"


@app.route("/hoth")
def hoth():
    time.sleep(random.random() * 0.6)
    return "ok"


@app.route("/coruscant")
def coruscant():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/yavin4")
def yavin4():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/dantooine")
def dantooine():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/corellia")
def corellia():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/sullust")
def sullust():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/ansion")
def ansion():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/bastion")
def bastion():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/gralle")
def gralle():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/empire")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 5001, threaded=True)
