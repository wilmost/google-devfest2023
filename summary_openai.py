import openai
import os
import datetime

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
    



current_date = datetime.datetime.now() 
formatted_date = current_date.strftime("%Y-%m-%d") 
filename = f"summary_{formatted_date}.txt"


with open("output1", 'r') as file:
     file_content = file.read()

file_generator(filename,summary_openai(file_content))