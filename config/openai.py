import openai
from env.env import *

def openai_config(content2):
    openai.api_key = OPENAI_KEY
    model_engine = "text-davinci-002"
    completion = openai.Completion.create(
        engine=model_engine, 
        prompt=content2,
        max_tokens=1024, 
        n=1,
        stop=None,
        temperature=0.5)


    response = completion.choices[0].text


    return response