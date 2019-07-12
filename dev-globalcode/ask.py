import pyowm

def weather():
	place = input("where are you located?: ")
	owm = pyowm.OWM('5d79007c8983dc94d876fe2454453581')
	observation = owm.weather_at_place(place)
	w = observation.get_weather()

	print (w.get_wind())
	print (w.get_humidity())

weather()
