import os, json
from dotenv import load_dotenv

# https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#emotion
# GET ENV VARS
load_dotenv()
API_KEY = os.getenv("API_KEY2")
URL = os.getenv("URL2")

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import (
    Features,
    CategoriesOptions,
    EmotionOptions,
)

authenticator = IAMAuthenticator(API_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version="2021-08-01", authenticator=authenticator
)

natural_language_understanding.set_service_url(URL)

# response = natural_language_understanding.analyze(
#     url="www.ibm.com", features=Features(categories=CategoriesOptions(limit=3))
# ).get_result()

response = natural_language_understanding.analyze(
    html="I dont know if i can keep living like this, this life is so boring and fucking miserable, I still love her though",
    features=Features(emotion=EmotionOptions(targets=["life", "her"])),
).get_result()

print(json.dumps(response["emotion"], indent=2))
