from api import API

# IBM Sentiment classifier model API
PREDICT_URL = "http://max-text-sentiment-classifier.max.us-south.containers.appdomain.cloud/model/predict"
# Initialize class
api = API(PREDICT_URL)
# Headers from the API Class
headers = api.HEADERS
# Create parameters from the API Class method
param = api.create_param(["That is good", "i wanna die"])
# Send a post request
resp = api.post(param, headers)
# Get the predictions from the response of the POST request
predictions = api.get_predictions(resp)
# Get the highest predictions
highest = api.get_highest_prediction(predictions)

