from api import API

# IBM Sentiment classifier model API
PREDICT_URL = "http://max-question-answering.max.us-south.containers.appdomain.cloud/model/predict"
'''
Sample input
paragraphs": [
    {
      "context": "John lives in Brussels and works for the EU",
      "questions": [
        "Where does John Live?",
        "What does John do?",
        "What is his name?"
      ]
    }
]
'''


# Initialize class
api = API(PREDICT_URL)
# Headers from the API Class
headers = api.HEADERS
# Create parameters from the API Class method
param = api.create_qna("John lives in Brussels and works for the EU", ["Where does John Live?", "What does John do?"])
# Send a post request
resp = api.post(param, headers)
# Get the predictions from the response of the POST request
predictions = api.get_answers(resp, show=True)

print(predictions)

