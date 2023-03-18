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


 

# Load Rasa agent and Spacy NLP model
agent = Agent.load("./rasa/models/20230318-022945-frosty-map.tar.gz")
nlp = spacy.load("en_core_web_sm")

# Load ScienceBot components
hash_table = HashTable(prehashed=science_defintions)
science_bot = ScienceBot(agent, nlp, hash_table, bot_responses, greetings, answer_style)

def config(configuration: ConfigClass):
    # TODO Add code here
    pass


async def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    response = ""

    for text in request.text:
        doc = science_bot.nlp(text)
        response = await science_bot._handle_message(doc)

        output.append(response)

    return SimpleText(dict(text=output))
