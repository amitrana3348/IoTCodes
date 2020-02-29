from sense_hat import SenseHat
from urllib.request import urlopen
import time
url = "https://api.thingspeak.com/update?api_key=W6CYQ8M6FTMHDN4C"
sense = SenseHat()

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    temp = round(temp,2)
    humidity = round(humidity,2)
    pressure = round(pressure,2)
    url_new = url + "&field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    print(url_new)
    response = urlopen(url_new)
    print(response.code)
    print("***************************************\n")
    time.sleep(15)