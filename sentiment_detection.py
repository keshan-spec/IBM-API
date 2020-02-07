from api import API


PREDICT_URL = "http://max-text-sentiment-classifier.max.us-south.containers.appdomain.cloud/model/predict"
api = API(PREDICT_URL)
headers = api.HEADERS
param = api.create_param(["That is good", "i wanna die"])
resp = api.post(param, headers)
pred = api.get_predictions(resp)

highest = api.get_highest_prediction(pred, show=True)
print(highest.items())
