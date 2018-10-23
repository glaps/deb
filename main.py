from bt import Bt24
from bottle import Bottle, request
import requests as r
from config import *
import json

app = Bottle()

class MyExe(Exception):
    def __init__(self, arg):
        self.arg = arg
def setinfo(num):
    for i in num:
        if i["deb"] > 0.0:
            JSONPOST["MESSAGE"] = MASS.format(i["patientName"],i["deb"])
            Bt24(JSONPOST, Bt_toking).send()

@app.route("/phone", method="post")
def insdex():
    try:
        phone = request.json.get("phone")
        if not phone: raise MyExe(phone)
        JSONGET["phoneNum"] = phone
    except json.decoder.JSONDecodeError:
        l.warning("no number")
        return "no number"
    except MyExe as exe:
        return "myEXE status %s!(" % exe
    try:
        qer = r.post(METHOD, json=JSONGET).json()
        setinfo(qer)
        resul = "|".join([" ".join(y) for y in [[i["patientName"],str(i["deb"])] for i in qer]])
        l.info("Number = %s informations = %s",phone, resul)
        return "ok"
    except json.decoder.JSONDecodeError:
        if phone:
            l.warning("%s %s !!!" %("error", phone))
        return "sorry bad num"
@app.route("/phone", method="get")
def rtrt():
    return "I am Work right now!"



