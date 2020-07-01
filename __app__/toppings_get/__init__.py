import azure.functions
from ..data_types.Toppings import Toppings
import json


def main(req: azure.functions.HttpRequest) -> str:
    return json.dumps(Toppings)
