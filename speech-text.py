# Import the Speech-to-Text client library
from google.cloud import speech, storage
from google.protobuf import wrappers_pb2

bucket_name = "wonderful-site"
destination_blob_name= "transcripts/bonao_transcript"
gcs_uri="gs://wonderful-site/audios/bonao_sample.wav"



# Instantiates a client
client=speech.SpeechClient()


def transcribe_speech():
  audio=speech.RecognitionAudio(uri=gcs_uri)

  config=speech.RecognitionConfig(
  #encoding=speech.RecognitionConfig.AudioEncoding.MP3,
  sample_rate_hertz=48000,
  language_code="es-MX",
  model="default",
  audio_channel_count=2,
  enable_word_time_offsets=True,
  )

  # Detects speech in the audio file
  operation=client.long_running_recognize(config=config, audio=audio)

  print("Waiting for operation to complete...")
  response=operation.result(timeout=90)

  for result in response.results:
    upload_to_bucket(bucket_name,destination_blob_name, result.alternatives[0].transcript)
    print("Transcript: {}".format(result.alternatives[0].transcript))


def upload_to_bucket(bucket_name,destination_blob_name, content): 
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(content, content_type="text/plain")

  
  
  
  
  

transcribe_speech()