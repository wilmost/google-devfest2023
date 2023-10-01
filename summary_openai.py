import openai
import os
import datetime
from google.cloud import storage

bucket_name = "wonderful-site"
destination_blob_name= "summaries/bonao-summary"
file_content= "gs://wonderful-site/transcripts/bonao_transcript"
openai.api_key =os.getenv("OPENAI_API_KEY")
 #os.getenv("OPENAI_API_KEY")

# Generate a summary of the input text using OpenAI's GPT-3.5 model and return a summary of the input text
def summary_openai(input_text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                {"role": "system", "content": "Make a summary of the following:"},
                {"role": "user", "content": input_text}
            ]
    )
    summary = (completion.choices[0].message.content)
    return summary 

# generte a txt file  wit a given name and content
def file_generator(file_name,file_content):
    with open(file_name, 'w') as file:
        file.write(file_content)
    return
  
    
def upload_to_bucket(bucket_name,destination_blob_name, content): 
    
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(content, content_type="text/plain")




current_date = datetime.datetime.now() 
formatted_date = current_date.strftime("%Y-%m-%d") 
filename = f"summary_{formatted_date}.txt"



upload_to_bucket(bucket_name, destination_blob_name, summary_openai(file_content))