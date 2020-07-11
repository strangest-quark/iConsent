from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import boto3
import json

app = Flask(__name__)
CORS(app)

lambda_client = boto3.client('lambda')


@app.route("/video", methods=['GET', 'POST'])
@cross_origin()
def video():
    input_map = request.get_json()
    print(input_map)
    req = {"req": input_map}
    url = lambda_client.invoke(FunctionName="video-generator",
                               InvocationType='RequestResponse',
                               Payload=json.dumps(req)
                               )
    url = json.loads(url['Payload'].read())
    res = {"url": url}
    return jsonify(res)


if __name__ == "__main__":
    app.run()
