import json
import boto3
import jwt
import os
from urllib.parse import urlparse

def lambda_handler(event, context):
    print(event)
    # return cors headers for preflight check
    if event['routeKey'] == "OPTIONS /{proxy+}":
        print(json.dumps({"step": "preflight", "message": "preflight CORS check"}))
        return {
            "headers": {
                "Access-Control-Allow-Headers": "*, Authorization",
                "Access-Control-Allow-Origin": "https://3000-omenking-awsbootcampcru-2n1d6e0bd1f.ws-us94.gitpod.io",
                "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
            },
            "statusCode": 200
        }
    else:
        token = event['headers']['authorization'].split(' ')[1]
        print(json.dumps({"step": "presignedurl", "access_token": token}))

        body_hash = json.loads(event["body"])
        extension = body_hash["extension"]

        decoded_token = jwt.decode(token, algorithms=['HS256'], options={"verify_signature": False})
        cognito_user_uuid = decoded_token['sub']


        s3 = boto3.client('s3',config=boto3.session.Config(signature_version='s3v4'))
        bucket_name = os.environ["UPLOADS_BUCKET_NAME"]
        object_key = f"{cognito_user_uuid}.{extension}"

        print(json.dumps({"object_key": object_key}))

        s3_client = boto3.client("s3")
        url = s3_client.generate_presigned_url(
            "put_object",
            Params={"Bucket": bucket_name, "Key": object_key,"ContentType": "image/jpeg"},
            ExpiresIn=60 * 5
        )
        body = json.dumps({"url": url})
        print(f"URL={url}")
        return {

            "statusCode": 200,
            "body": body
        }

