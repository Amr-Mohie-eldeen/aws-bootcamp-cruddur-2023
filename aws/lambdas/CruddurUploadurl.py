import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3',config=boto3.session.Config(signature_version='s3v4'))
    bucket_name = 'assets.amrmohie.cloud'
    folder_name = 'avatars/'
    file_key = event['file_name']
    if not file_key.endswith('.jpg'):
        return {'error': 'File name must end with .jpg'}
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_key,
        },
        ExpiresIn=3600 # URL will expire in 1 hour
    )
    return {'presigned_url': presigned_url}