import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random, threading, json
from datetime import datetime
import time

#====================================================
# MQTT Settings 
MQTT_Broker = "192.168.1.106"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "test_channel"



import paho.mqtt.client as mqttClient
import time

def on_subscribe(client, obj, mid,granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
        #print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
 
def on_message(client, userdata, message):
    print ("message received")
    abc = str(message.payload)
    print (abc)
    abc2 = abc.split("'")
    mydata2 = abc2[1].split("\\")
    print (mydata2)
    mydata2 = str(mydata2)
    mydata2 = mydata2.replace('[','')
    mydata2 = mydata2.replace(']','')
    mydata2 = mydata2.replace('\'','')
    print("done with it")
    num = int(mydata2)# this num is the response from Server as 0 or 1
    print(num)
    

def on_publish(client, obj, mid):
    print("mid: " + str(mid))
 
Connected = False   #global variable for the state of the connection
 
broker_address= "192.168.0.11"  #Broker address
port = 1883                         #Broker port
 
client = mqttClient.Client("Python")               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
client.subscribe("t1")
print('connected')
tCount = 1#this is the Termianl Identifier
try:
    while True:
        time.sleep(1)
        mystr = str(tCount) + "," + "123,1,01-09-2019,09:34:05,440-580,0,200,3,RF,SHA,105,RAMA"
        publish.single(MQTT_Topic, mystr, hostname=MQTT_Broker)
        #(result,mid)=client.publish(MQTT_Topic,mystr,2)
        #publish_Fake_Sensor_Values_to_MQTT()
        print("done")
        time.sleep(10)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()


#====================================================
