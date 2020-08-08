import json
import boto3

lambda_client = boto3.client('lambda')

def main(event, context):
    input_map = event['req']
    url = lambda_client.invoke(FunctionName="video-generator",
                               InvocationType='RequestResponse',
                               Payload=json.dumps(input_map)
                               )
    url = json.loads(url['Payload'].read())
    res = {"url": url}
    return res