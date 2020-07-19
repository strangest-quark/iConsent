from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import boto3
import json
from process import process

app = Flask(__name__)
CORS(app)

lambda_client = boto3.client('lambda')


@app.route("/video", methods=['POST'])
@cross_origin()
def video():
    input_map = request.get_json()
    req = {"req": input_map}
    url = lambda_client.invoke(FunctionName="video-generator-dev-app",
                               InvocationType='RequestResponse',
                               Payload=json.dumps(req)
                               )
    url = json.loads(url['Payload'].read())
    res = {"url": url}
    return jsonify(res)


@app.route("/dashboard", methods=['POST'])
@cross_origin()
def dashboard():
    dashboard_obj = request.get_json()
    print(dashboard_obj)
    res_map = process(dashboard_obj)
    return jsonify(res_map)


if __name__ == "__main__":
    app.run()
