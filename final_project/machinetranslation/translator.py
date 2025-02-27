'''Translator program'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authentificators import IAMAuthentificator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Setup Service
authentificator = IAMAuthentificator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authentificator=authentificator)
lt.set_service_url(url)

#English to French translation function
def english_to_french(english_text):
    '''English to French translation function'''
    translation = lt.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
    
    
#French to English translation function
def french_to_english(french_text):
    '''French to English translation function'''
    translation = lt.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
  
