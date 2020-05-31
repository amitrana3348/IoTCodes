from twython import Twython

from sense_hat import SenseHat #improting the sense HAT library

import time
sense = SenseHat()

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

while True:
    temp = sense.get_temperature()
    temp = round(temp,2)
    message = "My Room Temperature = " + str(temp)
    twitter.update_status(status=message)
    print("Tweeted: {}".format(message))
    time.sleep(15)

