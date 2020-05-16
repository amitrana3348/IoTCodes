import paho.mqtt.publish as publish
import time
MQTT_SERVER = "broker.mqttdashboard.com"
MQTT_PATH = "amit-temp"  # TOPIC
import random
temp = 0
while True:
    try:
        print("Making a send attempt\n")
        temp = str(random.randint(20,40))   # replace by any sensor information
        print('value is ',temp)
        a = publish.single(MQTT_PATH, temp, hostname=MQTT_SERVER, port=1883)
        print(a)
        print("value published")
        time.sleep(5)
    except ConnectionRefusedError:
        print("issue in connection")
    except TimeoutError:
        print("Time out, means network issue or no connectivity")
    except OSError:
        print("My own network is down")
    time.sleep(2)
    print("\nIteration Done\n*********************")
    
