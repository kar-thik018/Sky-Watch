import requests
from flask import Flask,render_template,redirect,request


app=Flask('__name__')
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def main(city):
    apikey="342d5a92c1ca16b286cabb20b770ae37"
    weatherdata=get_weather(city,apikey)
    print(weatherdata)
    return weatherdata['weather'][0]['main']

@app.route("/",methods=['POST','GET'])
def index():
    data=""
    if request.method=='POST':
        city=request.form['city']
        data=main(city)

    return render_template('index.html',data=data)


if __name__=='__main__':
    app.run(debug=True)