from urllib.request import urlopen
import random
import time
url = "https://api.thingspeak.com/update?api_key=W6CYQ8M6FTMHDN4C"

while True:
    temp = random.randint(20,35)
    humidity = random.randint(30,45)
    pressure = random.randint(10000,12000)
    url_new = url + "&field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    print(url_new)
    response = urlopen(url_new)
    print(response.code)
    print("***************************************\n")
    time.sleep(15)

