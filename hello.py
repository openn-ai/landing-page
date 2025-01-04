import json


def lambda_handler(event, context):
    """
    AWS Lambda function to echo the HTTP request.
    """
    # Log the incoming event
    print("Event:", json.dumps(event, indent=4))

    # Extract details from the event
    http_method = event.get("httpMethod", "UNKNOWN")
    path = event.get("path", "/")
    headers = event.get("headers", {})
    query_params = event.get("queryStringParameters", {})
    body = event.get("body", "")

    # Construct the response
    response = {
        "httpMethod": http_method,
        "path": path,
        "headers": headers,
        "queryStringParameters": query_params,
        "body": body,
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({
            "message": "Echoing your request!",
            "requestDetails": response,
        }),
    }
