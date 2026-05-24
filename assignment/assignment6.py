import requests


OPENWEATHER_API_KEY = "b8f77aa661cf819ed1e9ae766705c79c"  # already used in your repo


def openweather_weather_report(city: str) -> dict:
    """Fetch and return a richer OpenWeather 'current weather' report."""
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()

    # Safe extraction with fallbacks
    weather0 = (data.get("weather") or [{}])[0]
    main = data.get("main") or {}
    sys = data.get("sys") or {}
    wind = data.get("wind") or {}
    clouds = data.get("clouds") or {}

    report = {
        "city": data.get("name"),
        "country": sys.get("country"),
        "timezone": data.get("timezone"),
        "lat": (data.get("coord") or {}).get("lat"),
        "lon": (data.get("coord") or {}).get("lon"),
        "observation": {
            "status": weather0.get("main"),
            "description": weather0.get("description"),
            "icon": weather0.get("icon"),
        },
        "temperature": {
            "temp": main.get("temp"),
            "feels_like": main.get("feels_like"),
            "temp_min": main.get("temp_min"),
            "temp_max": main.get("temp_max"),
            "humidity": main.get("humidity"),
        },
        "pressure": {
            "pressure": main.get("pressure"),
            "sea_level": main.get("sea_level"),
            "grnd_level": main.get("grnd_level"),
        },
        "wind": {
            "speed": wind.get("speed"),
            "deg": wind.get("deg"),
            "gust": wind.get("gust"),
        },
        "clouds": {
            "all": clouds.get("all"),
        },
        "sys": {
            "sunrise": sys.get("sunrise"),
            "sunset": sys.get("sunset"),
            "type": sys.get("type"),
        },
    }

    return report


def print_weather_report(report: dict) -> None:
    print("\n=== OpenWeather Current Weather (Expanded) ===")
    print(
        f"Location: {report.get('city')} ({report.get('country')}) "
        f"lat={report.get('lat')} lon={report.get('lon')}"
    )

    obs = report.get("observation") or {}
    print(
        "Condition: "
        f"{obs.get('status')} - {obs.get('description')} "
        f"(icon={obs.get('icon')})"
    )

    temp = report.get("temperature") or {}
    print(
        "Temperature (°C): "
        f"temp={temp.get('temp')} feels_like={temp.get('feels_like')} "
        f"min={temp.get('temp_min')} max={temp.get('temp_max')}")
    print(f"Humidity: {temp.get('humidity')}%")

    pressure = report.get("pressure") or {}
    print(
        "Pressure (hPa): "
        f"pressure={pressure.get('pressure')} "
        f"sea_level={pressure.get('sea_level')} grnd_level={pressure.get('grnd_level')}"
    )

    wind = report.get("wind") or {}
    print(
        "Wind: "
        f"speed={wind.get('speed')} deg={wind.get('deg')} gust={wind.get('gust')}"
    )

    clouds = report.get("clouds") or {}
    print(f"Clouds: {clouds.get('all')}%")

    sys = report.get("sys") or {}
    print(f"Sunrise (unix): {sys.get('sunrise')}  Sunset (unix): {sys.get('sunset')}")


# --------- Extra free API calls (no key) ---------

def open_meteo_weather(lat: float, lon: float) -> dict:
    """Fetch current weather from Open-Meteo (no API key)."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
        "&timezone=auto"
    )
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.json()


def rest_countries_random_activity() -> dict:
    """Fetch free trivia using Numbers API (no key)."""
    # Using Numbers API is simpler than random countries; it returns text.
    url = "http://numbersapi.com/42/date"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return {"numbersapi": r.text}


def print_open_meteo_summary(payload: dict) -> None:
    print("\n=== Open-Meteo (Free, No-Key) ===")
    current = payload.get("current") or {}
    print(f"Time: {payload.get('current_time')} (auto timezone)")
    print(
        "Current: "
        f"temp={current.get('temperature_2m')}°C "
        f"feels_like={current.get('apparent_temperature')}°C "
        f"humidity={current.get('relative_humidity_2m')}% "
        f"wind_speed={current.get('wind_speed_10m')} km/h "
        f"weather_code={current.get('weather_code')}")


def print_numbersapi_summary(payload: dict) -> None:
    print("\n=== Numbers API (Free Trivia) ===")
    print(payload.get("numbersapi"))


# --------- Sudoku (console solver) ---------

def print_grid(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("------+-------+------")
        row = []
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row.append("|")
            row.append(str(grid[r][c]) if grid[r][c] != 0 else ".")
        print(" ".join(row))


def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None


def is_valid(grid, r, c, val):
    # row
    if any(grid[r][x] == val for x in range(9)):
        return False
    # col
    if any(grid[x][c] == val for x in range(9)):
        return False
    # box
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for rr in range(br, br + 3):
        for cc in range(bc, bc + 3):
            if grid[rr][cc] == val:
                return False
    return True


def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    r, c = empty

    for val in range(1, 10):
        if is_valid(grid, r, c, val):
            grid[r][c] = val
            if solve_sudoku(grid):
                return True
            grid[r][c] = 0
    return False


def run_sudoku_demo():
    # Example Sudoku (0 means empty)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("\n=== Sudoku Solver (Assignment 6) ===")
    print("Initial grid:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved grid:")
        print_grid(grid)
    else:
        print("No solution found for this Sudoku.")


def main():
    print("Assignment 6 - OpenWeather + Free APIs + Sudoku\n")

    city = input("Enter city for weather (e.g., London): ").strip()
    if not city:
        city = "London"

    try:
        report = openweather_weather_report(city)
        print_weather_report(report)

        # Call Open-Meteo using lat/lon from OpenWeather response
        lat = report.get("lat")
        lon = report.get("lon")
        if lat is not None and lon is not None:
            try:
                mete = open_meteo_weather(lat, lon)
                print_open_meteo_summary(mete)
            except Exception as e:
                print(f"\n(Open-Meteo call failed): {e}")

        # Another free API call
        try:
            trivia = rest_countries_random_activity()
            print_numbersapi_summary(trivia)
        except Exception as e:
            print(f"\n(NumbersAPI call failed): {e}")

    except Exception as e:
        print(f"\nOpenWeather call failed: {e}")

    run_sudoku_demo()


if __name__ == "__main__":
    main()

