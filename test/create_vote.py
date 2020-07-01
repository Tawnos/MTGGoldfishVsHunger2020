import uuid
import string
import random
from datetime import datetime
import json
import requests

def rand_str(n):
    return ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

def create():
    return {
        "user_id": str(uuid.uuid4()),
        "toppings": [
            {
                "count": 2,
                "value": ["foo","bar","baz"]
            },
            {
                "count": 1,
                "value": ["abc","def"]
            }
        ],
        "decks": [
            {
                "count": 1,
                "value": random.randint(100000000,999999999),
            }
        ]
    }
    
with open('../local.settings.json', 'r') as settingsFile:
    settings = json.load(settingsFile)

    function_url = 'https://mtggoldfishvshunger2020.azurewebsites.net/api/webhook/donation_received?code=D7j9evA1lPFWcEenDFaP8uEMp9l0KBBUYGApGFQAia7jDeonzMghlA=='

    r = requests.post(function_url, json=create())
    print(r.status_code, r.reason, r.text)

