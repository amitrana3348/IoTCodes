from twython import Twython

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

message = "Edureka is an e-learning platform"
with open('[file path]', 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)
