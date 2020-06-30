import azure.functions
from ..common.cosmos_client import DB
from ..data_types import Donation


def main(req: azure.functions.HttpRequest) -> str:
    req_body = req.get_json()

    donation = Donation.Donation(
        req_body["id"],
        req_body["user_id"],
        req_body["organization_id"],
        req_body["organization_name"],
        req_body["amount"],
        req_body["metadata"],
        req_body["created_at"]
    )

    if req_body["topic"] == "donation/created":
        DB.Donations.create_item(body=donation)

    return azure.functions.HttpResponse()
