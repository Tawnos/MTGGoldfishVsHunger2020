import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.route_params.get('id')

    if not id:
        return func.HttpResponse(
            "Please pass an id",
            status_code=400
        )
