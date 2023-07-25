#!/usr/bin/env python3
import os
import json
import openai

from config import API_KEY, ORG_ID
from oruch_chaim_sections import CATEGORIES_LIST

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    answer = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return answer.choices[0].message["content"]


openai.organization = ORG_ID
openai.api_key = API_KEY
#openai.Model.list()

MODEL = "gpt-3.5-turbo"

#question = "If I am eating a meal with three men, and one of them benches, am I stil obligated in zimun? "
question = "If my wife is in niddah, am I allowed to touch her?"
#question = "can I eat meat betwean rosh chodesh Av and the 9th of Av?"
#question = "what blessing do I make on a lemon?"


for categories in CATEGORIES_LIST:
    prompt = f"""You will be provided with a halachic question delimited by \
angle brackets. You will also be provided with a table of contents from \
Shulchan Aruch delimited by angle brackets. Each chapter has a chapter \
number followed by its name and a short summary of what it contains. Identifiy \
the chapter from the table of contents that contains the answer to the halachic \
question that you are given. Follow the steps below to get the correct answer.

Step 1: Use only the chapter summeries to find the exact chapter that you are sure contains the answer. \
Step 2: Determain if there is a chapter that you are absolutley certain contains the answer \
to the halachic question \
Step 3: If you are found a chapter that contains the answer to the halachic question output \
it in JSON format with the keys: number, title \
Step 4: If you did not find a chapter that contains the answer to the halachic question, \
use the same JSON keys: number and title, but leave the data fields blank. \

Question: <{question}>
Shulchan Aruch table of contents: <{categories}>
"""
    response = get_completion(prompt, MODEL)
    json_response = json.loads(response)
    print("one attempt")
    if len(json_response["title"]) > 0 :
        break

if len(json_response["title"]) > 0 :
    print(json_response["number"], " : ", json_response["title"] )

else :
    print("Uh oh, this isnt geshmak, I dont have a teshuva to your shaila, sorry.")
