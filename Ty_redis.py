from flask import Flask
from config import *
from flask import *
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Ty redis page!"


@app.route("/index" , methods=['POST', 'GET'])
def index():
    res = "tingyun"
    if request.method == 'POST':
        operate_type = request.form['type']
        if operate_type == "get":
            ret = requests.post('http://127.0.0.1:18888/snapchat/snapchat' , data = { 'Type': 'get'})
            if ret.status_code == 200:
                res = ret.content.decode()
            else:
                res = "operator get banned_key 【sc:hash:banned:user】 failed"
                
        elif operate_type == "add":
            uid = request.form['uid']
            res = requests.post('http://127.0.0.1:18888/snapchat/snapchat' , data = { 'Type': 'add' , 'uid' : uid}) 
            if res.status_code == 200:
                res = "operator add uid 【%s】 ok"%(uid)
            else:
                res = "operator add uid 【%s】 failed"%(uid)


        elif operate_type == "remove":
            uid = request.form['uid']
            res = requests.post('http://127.0.0.1:18888/snapchat/snapchat' , data = { 'Type': 'remove' , 'uid' : uid})
            if res.status_code == 200:
                res = "operator remove uid 【%s】 ok"%(uid)
            else:
                res = "operator remove uid 【%s】 failed"%(uid)

        else:
            res = "method not valid"
    
    return render_template('index.html', data=res)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=18889 ,debug=True)

