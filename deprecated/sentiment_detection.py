from api import API

# IBM Sentiment classifier model API
PREDICT_URL = "http://max-text-sentiment-classifier.max.us-south.containers.appdomain.cloud/model/predict"
# Sample input ["That is good", "i wanna die"]
#                 positive          negative


def get_text():
    inp = input("Enter your text > ")
    return main([inp])


def main(data):
    # Initialize class
    api = API(PREDICT_URL)
    # Headers from the API Class
    headers = api.HEADERS
    # Create parameters from the API Class method
    param = api.create_param(data)
    # Send a post request
    resp = api.post(param, headers)
    # Get the predictions from the response of the POST request
    predictions = api.get_predictions(resp)
    # Get the highest predictions
    highest = api.get_highest_prediction(predictions)
    # print the highest prediction
    print(highest)

    choice = input("Try again ? (y/n) > ")
    if choice.lower() in ["y", "yes"]:
        get_text()
    else:
        return


get_text()


