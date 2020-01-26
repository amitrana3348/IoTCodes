from urllib.request import urlopen
from time import sleep

#response = urlopen("https://www.google.com/")
#print(response.code)
#print("***************************************")

url = "https://api.thingspeak.com/update?api_key=QYALU2DH2Y5MNQMW"
temp = 23
humidity = 75
pressure = 60300

while True:
    mystring = url + "&field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    print (mystring)
    response = urlopen(mystring)
    print(response.code)
    print("*******************************\n")
    sleep(15)
