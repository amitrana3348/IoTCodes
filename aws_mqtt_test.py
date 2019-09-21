import paho.mqtt.client as mqtt
import ssl, random
from time import sleep

mqtt_url = "a1f7vy2goilgqr-ats.iot.ap-south-1.amazonaws.com"
root_ca = 'AmazonRootCA1.pem'
public_crt = '2d85b4c0c8-certificate.pem.crt'
private_key = '2d85b4c0c8-private.pem.key'

connflag = False


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    
def on_connect(client, userdata, flags, response_code):
    global connflag
    connflag = True
    print("Connected with status: {0}".format(response_code))
    client.subscribe("my/greenhouse")
     
def on_publish(client, userdata, mid):
    print (userdata + " -- " + mid)
    #client.disconnect()


if __name__ == "__main__":
    print ("Loaded MQTT configuration information.")
    print ("Endpoint URL: " + mqtt_url)
    print ("Root Cert: " + root_ca)
    print ("Device Cert: " + public_crt)
    print ("Private Key: " + private_key)

    client = mqtt.Client()
    client.tls_set(root_ca,
                   certfile = public_crt,
                   keyfile = private_key,
                   cert_reqs = ssl.CERT_REQUIRED,
                   tls_version = ssl.PROTOCOL_TLSv1_2,
                   ciphers = None)

    client.on_connect = on_connect
#    client.on_publish = on_publish

    print ("Connecting to AWS IoT Broker...")
    client.connect(mqtt_url, port = 8883, keepalive=60)
    client.on_message = on_message
    client.loop_start()
#    client.loop_forever()

    while 1==1:
        sleep(20)
        print (connflag)
        if connflag == True:
            print ("Publishing...")
            ap_measurement = random.uniform(25.0, 150.0)
            client.publish("my/ActivePower", ap_measurement, qos=1)
            print("ActivePower published: " + "%.2f" % ap_measurement )
        else:
            print ("waiting for connection...")
