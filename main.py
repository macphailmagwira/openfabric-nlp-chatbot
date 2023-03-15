import os
import random
import warnings
import asyncio
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
import spacy
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from rasa.core.agent import Agent

greetings = [
    "hey",
    "hello",
    "hi",
    "hello there",
    "good morning",
    "good evening",
    "moin",
    "hey there",
    "let's go",
    "hey dude",
    "goodmorning",
    "goodevening",
    "good afternoon"
]


agent = Agent.load("./rasa/models/20230315-142141-wood-mint.tar.gz")

nlp = spacy.load("en_core_web_sm")

def config(configuration: ConfigClass):
    # TODO Add code here
    pass

async def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    response = ''
    for text in request.text:
        #doc = nlp(text)
        response = await agent.parse_message(message_data=text)
        
        
        
        if 'intent' in response and response['intent'] and 'name' in response['intent'] and response['intent']['name']:

            
            intent_name = response['intent']['name']
            
            if intent_name == 'greet':
                response = str(random.choice(greetings))

            elif intent_name == 'information':                
                response = '\nNow thats a science question\n'
                
            else:
                
                response = '\nthat doesnt seem to be a science question\n'
                    
   
        else:
             response = '\nI dont seem to understand you, please elaborate\n'
             
    output.append(response)

    return SimpleText(dict(text=output))


async def main():
    config(None)
    print("\n\nWelcome to ScienceBot! I'm here to help you with any questions you have about science.\n\n")
    
    while True:
        user_input = input("What's your question or topic of interest?\n")
        request = SimpleText(dict(text=[user_input]))
        result = await execute(request, None)
        print(str(result.text))
        
        if user_input.lower() == 'exit':
            break


if __name__ == '__main__':
    asyncio.run(main())
