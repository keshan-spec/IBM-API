import json
import requests

# PARAMS = ["In hindsight, I do apologize for my previous statement.", "FUCK YOU"]
# PARAMS = {"text": ["In hindsight, I do apologize for my previous statement.", "FUCK YOU"]}
PARAMS = "{\"text\": [\"In hindsight, I do apologize for my previous statement.\", \"FUCK YOU\" ]}"

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
PREDICT_URL = "http://max-toxic-comment-classifier.max.us-south.containers.appdomain.cloud/model/predict"
PREDICT_URL_SENTIMENT = "http://max-text-sentiment-classifier.max.us-south.containers.appdomain.cloud/model/predict"


class API:
    def __init__(self, url):
        self.url = url

    def post(self, data, headers=None):
        # response = requests.post(self.url, headers=headers, data=data)
        # return response if response.status_code == 200 else response.status_code
        return requests.post(self.url, headers=headers, data=data)

    def get(self, params, headers=None):
        return requests.get(self.url, headers=headers, params=params)

    @staticmethod
    def encode_json(string):
        return json.loads(string)

    @staticmethod
    def create_param(param):
        data = {"test": []}
        for i in param:
            data["test"].append(i)
        data = str(data).replace("'", '"').replace('"', '\"')
        return "\""+data+"\""

    def get_prediction(self):
        pass


api = API(PREDICT_URL)
post = api.post(PARAMS, HEADERS)
json_package = post.json()
# for i in range(0, 2):
#     pos = json_package["predictions"][i]["positive"]
#     neg = json_package["predictions"][i]["negative"]
#     print(f'For the {i + 1}th comment {int(float(pos if (pos > neg) else neg) * 100)}% ')

print(json_package["predictions"])

"""
using curl

curl -d "{ \"text\": [ \"The Model Asset Exchange is a crucial element of a developer's toolkit.\" ]}" -X POST "http://max-text-sentiment-classifier.max.us-south.c 
ontainers.appdomain.cloud/model/predict" -H "Content-Type: application/json"
"""
