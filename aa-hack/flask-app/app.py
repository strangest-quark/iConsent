from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import boto3
import json
from process import process, consent_res
import requests

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


@app.route("/consent", methods=['POST'])
@cross_origin()
def consent():
    session = request.headers['sessionId']
    consentArtefactId = request.headers['consentArtefactId']
    language = request.headers['language'][:2]
    return jsonify(consent_res(consentArtefactId, session, language))


@app.route("/dashboard", methods=['POST'])
@cross_origin()
def dashboard():
    session = request.headers['sessionId']
    url = 'https://api-sandbox.onemoney.in/app/dashboard'
    headers = {'sessionId': session, 'Content-Type': 'application/json'}
    req = requests.get(url, headers=headers)
    dashboard_obj =  json.loads(req.content)
    dashboard_obj['language'] = request.headers['language'][:2]
    dashboard_obj['session'] = request.headers['sessionId']
    print(dashboard_obj)
    res_map = process(dashboard_obj)
    return jsonify(res_map)


if __name__ == "__main__":
    app.run()
