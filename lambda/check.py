import json

import httpx


def handler(event, context):
    try:
        response = httpx.get("https://api.ipify.org?format=json")
        return {"statusCode": 200, "body": json.dumps(response.json())}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
