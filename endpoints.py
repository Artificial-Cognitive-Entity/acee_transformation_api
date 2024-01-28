from google.cloud import storage
from datetime import datetime
import json
import os
from errors import BucketAccessError, DataProcessingError


# TODO better error handling

def get_bucket_object(object_name):
    client = storage.Client("acee-sd")
    bucket = client.bucket("acee-raw-documents")

    try:
        blob = bucket.blob(object_name)
    except Exception as e:
        raise BucketAccessError(f"Error accessing bucket: {str(e)}")

    metadata = blob.metadata or None
    contents = blob.download_as_text()
    print("Retreieved Object Data:")

    # Do stuff 
    print(contents)


    # Embeddings

    upload_to_bucket(object_name, contents)
    return contents


def upload_to_bucket(object_name, object_data):
    client = storage.Client("acee-sd")
    bucket = client.bucket("acee-normalized-json")

    # Determine Directory Based on Source
    directory = ''
    # if object_data["document_data"].get("source_id") == "confluence":
    #     directory = 'confluence'

    # Remove file extension
    object_name = os.path.splitext(object_name)[0]

    # Generate a new file name
    file_name = f"{directory}/file_{datetime.now().strftime('%Y%m%d%H%M%S')}_{object_name}.json"

    # Convert the dictionary to a JSON string
    json_str = json.dumps(object_data, indent=4)

    # Create new blob for upload
    new_blob = bucket.blob(file_name)

    # Upload the JSON blob to the GCP bucket
    new_blob.upload_from_string(json_str, content_type='application/json')

    print(f"Uploaded JSON file to GCS: {file_name}")


#! JIRA

# Fields that need editing
    # 1 JSON file = 1 Jira Account (Org)

    # Data_Source
    #     Source_icon_url
    #     last_indexed_at

    # document   
    #     status (transformed)
    #     author_image_url
    
    # content
    #     embedding


#! CONFLUENCE
    
    # Data_Source
    #     Source_icon_url
    #     last_indexed_at
