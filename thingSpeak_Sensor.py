# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2020-01-26-08-50-04.py"
from urllib.request import urlopen

#from sense_emu import SenseHat
# use above line if you don't have a sense HAT
from sense_hat import SenseHat


from time import sleep
sense = SenseHat()

url = "https://api.thingspeak.com/update?api_key=QYALU2DH2Y5MNQMW"
sense.clear()
while True:
    humidity = sense.humidity
    humidity = round(humidity,2)
    temp = sense.temperature
    temp = round(temp,2)
    pres = sense.pressure
    pres = round(pres,2)
    
    
    mystring = url + "&field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pres)
    print (mystring)
    response = urlopen(mystring)
    print(response.code)
    print("*******************************\n")
    sleep(15)
