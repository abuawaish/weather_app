from flask import Flask , render_template, request
import requests 
import json
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("Index.html")

@app.route("/weatherapp",methods = ['POST' , "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    return json.dumps(data, sort_keys=True, indent=4)

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 5001)