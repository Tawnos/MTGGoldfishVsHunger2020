import azure.functions
from ..common.cosmos_client import DB
from ..data_types import Donation
import json


def main(req: azure.functions.HttpRequest) -> str:
    req_body = req.get_json()

    topic = req_body.get("topic") 
    data = req_body.get("data")
    
    donation = Donation.Donation(
        data["id"],
        data["user_id"],
        data["organization_id"],
        data["organization_name"],
        data["amount"],
        data["metadata"],
        data["created_at"]
    )

    donationJson = json.dumps(donation,default=lambda x: x.__dict__)

    if topic == "donation/created":
        DB.Donations.upsert_item(donation.__dict__)

    return f"{topic}: {donationJson}"
