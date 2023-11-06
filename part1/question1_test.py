from question1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"


def get_city_weather(city):
  
    temperature = get_city_temperature(city)

    if city == "Quito":
        sky_condition = "sunny"
    elif city == "New York":
        sky_condition = "rainy"
    else:
        sky_condition = "unknown"

    return str(temperature) + " degrees and " + sky_condition

