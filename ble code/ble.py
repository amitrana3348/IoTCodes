import configparser
from os import system
import time
#led1 = 21 #pin where you connect relay to raspberry pi 
#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(led1, GPIO.OUT)


def readConfig():
   global ble_id
   global scan_interval
   global p_threshold 
   global a_threshold
   
   configParser = configparser.RawConfigParser()   
   configFilePath = r'config.ini'
   configParser.read(configFilePath)
   ble_id = configParser.get('app-config', 'ble_id')
   scan_interval = int(configParser.get('app-config', 'scan_interval'))
   p_threshold = int(configParser.get('app-config', 'p_threshold'))
   a_threshold = int(configParser.get('app-config', 'a_threshold'))
   

   print("ble id = ",ble_id)
   print("scan time = ",scan_interval)
   print("p_thres = ",p_threshold)
   print("a_thres = ",a_threshold)
   

if __name__=='__main__':
   readConfig()
   on = 0
   off = 0
   status = "unknown"
   while True:
      command = "sudo timeout -s SIGINT {}s hcitool -i hci0 scan > devices.txt".format(scan_interval)
      system(command)
      print(command)
      found = False
      time.sleep(5)
      with open(r"devices.txt", "r") as file :
         for line in file:
            if str(ble_id) in str(line) :
               found = True
      if found == True: 
         if on < p_threshold: 
            on = on + 1
            off = 0
         print("present")
         print("On = ",on)
         print("Off = ",off)
      if found == False:
         if off < a_threshold: 
            off = off + 1
            on = 0
         print("absent")
         print("On = ",on)
         print("Off = ",off)
      if on == p_threshold and status != "on":
         status = "on"
         print("\n\nDevice On")
         #GPIO.output(led1, True) 
      if off == a_threshold and status != "off":
         status = "off"
         print("\n\nDevice Off")
         #GPIO.output(led1, False) 
      time.sleep(1)
