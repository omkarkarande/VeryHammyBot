import os
import json
import random
import twitter
from dotenv import load_dotenv

# # Load up the env vars
# load_dotenv()

# # Generate a twitter client
api = twitter.Api(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token_key=os.getenv("ACCESS_TOKEN_KEY"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

# Load the quotes and select a random one that is less than 280 chars long.
with open("./things.txt", "r") as f:
    things = f.readlines()

item_one = random.choice(things).strip().lower()
item_two = random.choice(things).strip().lower()

tweet = f'{item_one} is just like {item_two}'.capitalize()

# Tweet that shit
status = api.PostUpdate(tweet)
