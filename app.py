from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods=['POST', 'GET'])
def get_weatherdata():
    if request.method == 'POST':
        # Get the form data
        city = request.form.get('city')
        appid = request.form.get('appid')
        units = request.form.get('units')

        # Check if any of the form fields are empty
        if not city or not appid or not units:
            return "Please fill out all fields in the form."

        # Make the API request
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': appid,
            'units': units
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            city_name = data.get('name')
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            return f"Weather in {city_name}: {weather_description}, Temperature: {temperature}°C"
            return f"city :{city}"
        else:
            return "Failed to fetch weather data. Please check your input and API key."

    return "Please submit the form to get weather data."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
