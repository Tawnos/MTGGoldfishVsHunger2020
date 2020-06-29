import azure.functions

def main(req: azure.functions.HttpRequest) -> str:
    return 'Hello, world!'
    