from flask import Flask, render_template, request
import requests
from typing import Any
from requests import ConnectionError
from requests.models import Response
import os
from dotenv import load_dotenv

app: Flask = Flask(__name__)

@app.route('/')
def home_page() -> str:
    return render_template("index.html")

@app.route('/weather_app', methods=['GET', 'POST'])
def weather_app() -> str:
    weather_data: dict[str , Any] | None = {}
    error_message: str = ""
    try:
        if request.method == 'POST':
            city: str = request.form['city'].strip()
            city_name: str = ""
            for char in city:
                if char.isalpha() or char.isspace():
                    city_name += char
            city = city_name.strip()

            # Load environment variables from the .env file
            load_dotenv()
            api_key: str = os.getenv('api_key')
            weather_url: str = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response: Response = requests.get(weather_url)
            weather_data = response.json()
            if weather_data is not None:
                if weather_data['cod'] != 200:
                    error_message = weather_data.get('message', 'Error occurred')
                    weather_data = None  # Reset weather_data if there's an error
    except ConnectionError:
        exception_message: str = f"You are not connected to the internet."
        return render_template('index.html', weather = weather_data, error=exception_message)

    return render_template('index.html', weather = weather_data, error = error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
