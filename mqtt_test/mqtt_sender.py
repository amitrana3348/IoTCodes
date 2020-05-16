import paho.mqtt.publish as publish
import time
MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "temp"  # TOPIC
temp = 0
while True:
    try:
        print("Making a send attempt\n")
        t2 = str(temp)
        temp = temp+2
        a = publish.single(MQTT_PATH, t2, hostname=MQTT_SERVER, port=1883)
        print(a)
        time.sleep(2)
    except ConnectionRefusedError:
        print("issue in connection")
    except TimeoutError:
        print("Time out, means network issue or no connectivity")
    except OSError:
        print("My own network is down")
    time.sleep(2)
    print("\nIteration Done\n*********************")
    
