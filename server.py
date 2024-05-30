from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city("Saint-Petersburg,Russia")
    if weather:
        return (f"Температура: {weather['temp_C']}, "
                f"ощущается как {weather['FeelsLikeC']}")
    else:
        return f"Сервис погоды временно недоступен"


if __name__ == "__main__":
    app.run(debug=True)
