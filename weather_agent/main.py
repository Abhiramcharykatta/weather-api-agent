from enum import auto
import json

from dotenv import load_dotenv
from openai import OpenAI
import os

import requests



load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    else:
        return "Could not retrieve weather information."



# while True:
message = input(">>>")

messages = [
    {
        "role": "system",
        "content": """
        You are a weather assistant.

        Examples:
        User: What is the weather in Delhi?
        Action: Call get_weather with city="Delhi".

        User: Tell me the weather in Hyderabad.
        Action: Call get_weather with city="Hyderabad".

        Always use the get_weather tool for current weather questions.
        Do not invent weather information.
        """
    },
    {
        "role": "user",
        "content": message
    }
]

tools = [
    {   "type": "function",
        "function":{
            "name": "get_weather",
            "description": ("Get the current weather for a given city."
                            "Extract ONLY the city name from the user's query. "
                            "For example, if the user says "
                            "'get the current weather at Hyderabad', "
                            "the city argument must be 'Hyderabad', "
                            "not the entire sentence."),
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "only the city name eg. Delhi, Hyderabad, Mumbai, etc."
                    }
                },
                "required": ["city"]
            }
        }   
    }
]

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

assistant_message = response.choices[0].message

if assistant_message.tool_calls:
    for tool_call in assistant_message.tool_calls:
        if tool_call.function.name == "get_weather":
            arguments = json.loads(tool_call.function.arguments)
            city = arguments["city"]
            print(get_weather(city))
else:
    print(assistant_message.content)

# https://wttr.in/%7Bcity%7D?format=%C+%t






########### THE  CODE IS NOT GIVING THE OUTPUT AS EXPECTED ,I MEAN I CANT CHANGE THE OUTPUT FORMAT ,
# SO LOOK THE UDEMY VIDEO AND CHANGE THE CODE ACCORDINGLY 