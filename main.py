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
from knowlege_base.science_definitions import science_defintions
from functions.hash_table import HashTable
from science_bot.sciencebot import ScienceBot
from responses.responses import bot_responses
from responses.responses import greetings
from responses.responses import answer_style



agent = Agent.load("./rasa/models/20230315-161107-proper-torpedo.tar.gz")
nlp = spacy.load("en_core_web_sm")
hash_table = HashTable(prehashed=science_defintions)


def config(configuration: ConfigClass):
    # TODO Add code here
    pass


async def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    science_bot = ScienceBot(agent, nlp, hash_table, bot_responses,greetings,answer_style)
    output = []
    response = ""

    for text in request.text:
        doc = science_bot.nlp(text)
        response = await science_bot._handle_message(doc)

        output.append(response)

    return SimpleText(dict(text=output))


async def main():
    config(None)
    print(hash_table.get("atom"))
    print(
        "\n\nWelcome to ScienceBot! I'm here to help you with any questions you have about science. If you need to exit, remember to tell me\n\n"
    )
    while True:
        user_input = input("\n\nWhat's your question or topic of interest?\n")
        request = SimpleText(dict(text=[user_input]))
        result = await execute(request, None)

        print(result.text)

        if user_input.lower() == "exit":
            break


if __name__ == "__main__":
    asyncio.run(main())
