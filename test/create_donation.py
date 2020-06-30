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
        "topic": "donation/created",
        "data": {
            "id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "email": f"{rand_str(12)}@gmail.com",
            "first_name":rand_str(12),
            "last_name": rand_str(12),
            "organization_id": str(uuid.uuid4()),
            "organization_name": "American Red Cross",
            "amount": random.choice([5,10,20,50,100]),
            "phone_number": random.randint(100000000,999999999),
            "status": "processed",
            "external_id": random.randint(12345,9999999),
            "metadata": "arbitrary data string",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
            }
    }
    
with open('../local.settings.json', 'r') as settingsFile:
    settings = json.load(settingsFile)

    function_url = 'https://mtggoldfishvshunger2020.azurewebsites.net/api/webhook/donation_received?code=D7j9evA1lPFWcEenDFaP8uEMp9l0KBBUYGApGFQAia7jDeonzMghlA=='

    r = requests.post(function_url, json=create())
    print(r.status_code, r.reason, r.text)
    #donations = [create() for i in range(10)]


