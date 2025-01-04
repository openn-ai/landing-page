import json
from typing import Any


def lambda_handler(event: dict, context: Any) -> dict:
    """
    AWS Lambda function to echo the HTTP request.
    """
    # Log the incoming event
    print("Event:", json.dumps(event, indent=4))

    body = event.get("body", {"message": "Hello World"})

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({
            "message": "Echoing your request!",
            "response": body["message"],
        }),
    }
