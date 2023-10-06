from flask import escape
from google.cloud import storage

def upload_file_to_bucket(request):
    request_json = request.get_json(silent=True)
    bucket_name = request_json.get("bucket_name")
    source_file_name = request_json.get("source_file_name")
    destination_blob_name = request_json.get("destination_blob_name")

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    return f"File {source_file_name} uploaded to {bucket_name}/{destination_blob_name}"
