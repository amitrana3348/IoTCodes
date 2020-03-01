from twython import Twython
import random
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

messages = [
        "Hi Twitter",
        "Hello from Edureka",
        "Hello from my Raspberry Pi",
        "I'm a Pi Twitter Bot",
]
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: {}".format(message))
