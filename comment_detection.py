from api import API

PREDICT_URL = "http://max-toxic-comment-classifier.max.us-south.containers.appdomain.cloud/model/predict"
api = API(PREDICT_URL)
headers = api.HEADERS
param = api.create_param(["Fucking nigger"])
resp = api.post(param, headers)
pred = api.get_prediction(resp)
print(pred)
