from sense_hat import SenseHat
#from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
    temp = sense.get_temperature()
    temp = round(temp,2)
    print("Temp = ",temp)
    humidity = sense.get_humidity()
    humidity = round(humidity,2)
    print("Humidity = ",humidity)
    pressure = sense.get_pressure()
    pressure = round(pressure,2)
    print("Pressure = ",pressure)
    print("********************************************\n")
    time.sleep(3)
    