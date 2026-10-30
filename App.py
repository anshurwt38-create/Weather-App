
from flask import Flask,render_template,request,jsonify
request,jsonify
import requests
app=Flask(__name__)
API_KEY="1b02254cfddfe5d873903db7093f660f"
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/Weather')
def Weather():
    city=request.args.get('city')
    # return jsonify ({'city':city})

    if not city:
        return jsonify({"error":"City is required"})
    url=f"https://api.openweathermap.org/data/2.5/weather7q={city}&appid={API_KEY}&unit5=metric"
    
    res=requests.get(url)
    data=res.json()
    print("status code:",res.status_code)
    if data.get("cod")!=200:
        return jsonify({"error":data.get ("message","something went wrong")})
    
#clean response
    result={
        "city":data["name"],
    "temprature":data["main"]["temp"],
    "wind":data["wind"]["speed"],
    "humidity":data["main"]["humidity"],
    "weather condition":data["weather"][0]["main"],
    "pressure":data["main"]["pressure"],
    "sunrise":data["sys"]["sunrise"]
  }
    return jsonify(result)
if __name__=="__main__":
    app.run(debug=True)

