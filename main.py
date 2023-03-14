import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
import spacy

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

nlp = spacy.load("en_core_web_sm")

def config(configuration: ConfigClass):
    # TODO Add code here
    pass

def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        print(text + '\n')
        response = ''
        output.append(response)

    return SimpleText(dict(text=output))


def main():
    config(None)
    print("\n\nWelcome to ScienceBot! I'm here to help you with any questions you have about science.\n\n")
    
    while True:
     user_input = input("What's your question or topic of interest?\n")
     request = SimpleText(dict(text=[user_input]))
     result = execute(request, None)
     print(result.text)
     
     if user_input.lower() == 'exit':
            break


if __name__ == '__main__':
     main()
  
