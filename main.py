from bt import Bt24
from bottle import Bottle, request
import requests as r
from config import *
app = Bottle()



def setinfo(num):
    JSONPOST["MESSAGE"] = JSONPOST["MESSAGE"].format(num[0]["patientName"],num[0]["deb"])
    print(num,num[0]["deb"], type(num[0]["deb"]))
    if num[0]["deb"] > 0.0:
        Bt24(JSONPOST, Bt_toking).send()



@app.route("/phone", method="post")
def insdex():
    phone = str(request.json.get("phone"))
    JSONGET["phoneNum"] = phone

    try:
        setinfo(r.post(METHOD, json=JSONGET).json())
        l.info(phone)
    except :
        l.warning(phone)
        return "sorry bad num"
    return "ok"
@app.route("/phone", method="get")
def rtrt():
    return "I am Work right now!"
app.run(port=5555, debag=True)
