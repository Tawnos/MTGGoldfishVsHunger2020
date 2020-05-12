from common import common.globals
import azure.functions


def main(req: azure.functions.HttpRequest) -> str:
    return f'Hello, world!'
    