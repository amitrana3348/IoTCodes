import paho.mqtt.publish as publish
import time
MQTT_SERVER = "192.168.1.100"
MQTT_PATH = "temp"  # TOPIC
while True:
    try:
        print("Making a send attempt\n")
        a = publish.single(MQTT_PATH, "35", hostname=MQTT_SERVER)
        print(a)
        time.sleep(2)
    except ConnectionRefusedError:
        print("issue in connection")
    except TimeoutError:
        print("Time out, means network issue or no connectivity")
    except OSError:
        print("My own network is down")
    time.sleep(10)
    print("\nIteration Done\n*********************")
    
