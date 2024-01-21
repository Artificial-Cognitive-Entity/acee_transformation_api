from google.cloud import storage
import datetime
import json

def get_bucket_object(object_name):
    client = storage.Client("acee-sd")
    bucket = client.bucket("acee-raw-documents")
    blob = bucket.blob(object_name)
    metadata = blob.metadata or None
    contents = blob.download_as_text()
    print("Retreieved Object Data:")
    print(contents)
    return contents


def upload_to_bucket(object_name, object_data):


    client = storage.Client("acee-sd")
    bucket = client.bucket("acee-raw-documents")


    # Determine Directory Based on Source
    directory = ''
    if object_data["document_data"].get("source_id") == "confluence":
        directory = 'confluence'

    # Generate a file name
    file_name = f"{directory}/file_{datetime.now().strftime('%Y%m%d%H%M%S')}_{object_name}.json"

    # Convert the dictionary to a JSON string
    json_str = json.dumps(object_data, indent=4)

    # Upload the JSON string to the GCP bucket
    bucket.upload("acee-normalized-documents", object_name=file_name, data=json_str, mime_type='application/json')

    print(f"Uploaded JSON file to GCS: {file_name}")
