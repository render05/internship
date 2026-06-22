import requests

OPENWEATHER_API_KEY = "b8f77aa661cf819ed1e9ae766705c79c"  # from your existing code


def weather_data(city: str):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()

        main = data.get("main") or {}
        sys = data.get("sys") or {}
        wind = data.get("wind") or {}
        clouds = data.get("clouds") or {}
        coord = data.get("coord") or {}
        weather0 = (data.get("weather") or [{}])[0]

        print("\n=== OpenWeather: Expanded Weather Data ===")
        print(f"City: {data.get('name')} , Country: {sys.get('country')}")
        print(f"Coordinates: lat={coord.get('lat')} lon={coord.get('lon')}")
        print(
            "Condition: "
            f"{weather0.get('main')} - {weather0.get('description')} "
            f"(icon={weather0.get('icon')})"
        )

        print(
            "Temperature (°C): "
            f"temp={main.get('temp')} feels_like={main.get('feels_like')} "
            f"min={main.get('temp_min')} max={main.get('temp_max')}"
        )
        print(f"Humidity: {main.get('humidity')}%")

        # pressure fields
        print(
            "Pressure (hPa): "
            f"pressure={main.get('pressure')} sea_level={main.get('sea_level')} grnd_level={main.get('grnd_level')}"
        )

        print(f"Visibility (m): {data.get('visibility')}")
        print(
            "Wind: "
            f"speed={wind.get('speed')} m/s deg={wind.get('deg')} gust={wind.get('gust')}"
        )
        print(f"Cloudiness: {clouds.get('all')}%")

        print(f"Timezone (sec): {data.get('timezone')}")
        print(f"Sunrise (unix): {sys.get('sunrise')}  Sunset (unix): {sys.get('sunset')}")

    except requests.exceptions.RequestException as e:
        print("API error:", e)


city = input("enter city name: ").strip()
if city:
    weather_data(city)
else:
    print("No city entered.")

