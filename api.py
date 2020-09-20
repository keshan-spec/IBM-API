import os, json
from dotenv import load_dotenv

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# GET ENV VARS
load_dotenv()
API_KEY = os.getenv('API_KEY')
URL = os.getenv('URL')

utterances = [
    "Hello, I'm having a problem with your product.",
    "OK, let me know what's going on, please.",
    "Well, nothing is working :(",
    "Sorry to hear that.",
]

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

class API:
    def __init__(self, API_KEY, URL):
        # AUTH 
        authenticator = IAMAuthenticator(API_KEY)
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=authenticator
        )

        self.tone_analyzer.set_service_url(URL)

    '''
    This method is for longer and more meaningful sentences
    returns a dict/ json
    :arg
        text : the string to be processed
        verbose : bool to get detailed stats (default false)
    '''
    def analyse_tone(self, text: str, verbose: bool = False):
        mod_obj = {}
        sentences = []

        obj = self.tone_analyzer.tone(
            {'text': text},
            sentences=verbose,
            content_type='application/json'
        )
        result = obj.get_result()
        status = obj.get_status_code()

        if status == 200:
            if verbose:
                try:
                    for item in result["sentences_tone"]:
                        tones = {}
                        for i in item["tones"]:
                            tones[i["tone_name"]] = i["score"]
                        
                        sentences.append({"sentence": item["text"], "tones": tones})
                    
                    mod_obj["result"] = {
                        "sentences": sentences
                    }
                except KeyError:
                    pass
            
            doc_tone = {}
            for i in result["document_tone"]["tones"]:
                doc_tone[i["tone_name"]] = i["score"]

            mod_obj["result"] = {
                "text": text,
                "status": status,
                "overall": doc_tone
            }
            return mod_obj
        return status    


    '''
    This method is to analyze short phrases
    returns a dict/ json
    :arg
        text : the string to be processed
    '''
    def analyse_chat(self, text: str):
        mod_obj = {}
        tones = {}

        obj = self.tone_analyzer.tone_chat(
        [{'text': text}]
        )

        result = obj.get_result()
        status = obj.get_status_code()

        if status == 200:
            tmp = result["utterances_tone"][0]

            for i in tmp["tones"]:
                tones[i["tone_name"]] = i["score"]

            mod_obj["result"] = {
                "status": status,
                "text": tmp["utterance_text"],
                "tones": tones
            }
            return mod_obj
        return status


    '''
    -- prints the http codes definition
    :arg
        response: response code number
    '''
    @staticmethod
    def http_code(response):
        if response is None:
            return
        http_codes = {
            200: "Success",
            404: "Invalid URL page not found",
            400: "The browser (or proxy) sent a request that this server could not understand",
            405: "Restricted",
        }
        try:
            return http_codes.get(response, "Null")
        except Exception as e:
            print("Error : ", e)
            return


    '''
    Helper function to display the result
    '''
    @staticmethod
    def print(result):
        print(json.dumps(result, indent=2))

       
# create object
api = API(API_KEY, URL)
tone_analysis = api.analyse_tone(text, True) # verbose true
chat_analysis = api.analyse_chat(utterances[3]) # 3rd index of the list

# print results
api.print(tone_analysis)
api.print(chat_analysis)