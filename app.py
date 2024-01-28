from flask import Flask, request, jsonify, abort
from endpoints import *
import functools
import logging
from errors import BucketAccessError, DataProcessingError

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# BUILD
# sudo docker build -t acee_transformation_api .
# RUN
# docker run -p 8888:8888 -e PORT=8888 -v ~/.config/gcloud/application_default_credentials.json:/tmp/keys/application_default_credentials.json -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/application_default_credentials.json acee_transformation_api
# ONE COMMAND
# sudo docker build -t acee_transformation_api . && docker run -p 8888:8888 -e PORT=8888 -v ~/.config/gcloud/application_default_credentials.json:/tmp/keys/application_default_credentials.json -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/application_default_credentials.json acee_transformation_api

@app.route('/api/transform', methods=['POST'])
def process_bucket_object():
    data = request.json
    object_name = data['object_name']
    bucket_object = get_bucket_object(object_name)
    return bucket_object

@app.route('/test', methods=['GET'])
def tests():
    return "hello there"

#? ERROR HANDLING

@app.errorhandler(BucketAccessError)
def handle_bucket_access_error(error):
    logging.error(f"BucketAccessError: {error}")
    return jsonify({"error": str(error)}), 500

@app.errorhandler(DataProcessingError)
def handle_data_processing_error(error):
    logging.error(f"DataProcessingError: {error}")
    return jsonify({"error": str(error)}), 500
