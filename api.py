import requests
# 1) If parameter like this, use the create param method (RECOMMENDED)
# PARAMS = ["In hindsight, I do apologize for my previous statement.", "HARSH NEGAVTIVE"]

# 2) default parameter type, enclosed in single quotes with escaped strings
# PARAMS = '{"text": ["In hindsight, I do apologize for my previous statement.", "HARSH NEGAVTIVE"]}'

# 3) If parameter has apostrophe's or any quotation, use an escape string
# PARAMS = '{\"text\": [\"In hindsight, I do apologize for my previous statement.\", \"HARSH NEGAVTIVE\" ]}'


class API:
    # DEFAULT HEADER TYPE FOR APIs
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    def __init__(self, url):
        self.url = url
        self.data = {"text": []}

    '''
    Send post request to url with data and headers
    :arg 
        data : a data string formatted correctly to suit the APIs requirement (USE create_param method)
        headers : a dict of headers (Default none)
    :return : a requests object 
    '''
    def post(self, data, headers=None):
        try:
            response = requests.post(self.url, headers=headers, data=data)
            print(f"Status code : {self.http_code(response.status_code)}")
            return requests.post(self.url, headers=headers, data=data)
        except requests.exceptions.ConnectionError:
            print("[ERR] Connection error..")

    '''
    Send get request to url with params and headers
    :arg 
        params : a data string formatted correctly to suit the APIs requirement (USE create_param method)
        headers : a dict of headers (Default none)
    :return : a requests object 
    '''
    def get(self, params, headers=None):
        try:
            response = requests.get(self.url, headers=headers, params=params)
            print(f"Status code : {self.http_code(response.status_code)}")
            return response
        except requests.exceptions.ConnectionError:
            print("[ERR] Connection error..")

    '''
    Helper method to create parameters
    :arg  
        param : A list of string
    :return : string 
    '''
    def create_param(self, param):
        for i in param:
            self.data["text"].append(i.replace("'", ""))
        data = str(self.data).replace("'", '"')
        return data

    '''
    returns the highest predictions of the parameters
    :arg
        obj : the requests object
        show : bool to show or hide the printing (default false)
    '''
    def get_highest_prediction(self, obj, show=False):
        if obj is None:
            print("[ERR] Empty object at get_highest_prediction()")
            return
        highest = {}
        for i in range(len(obj)):
            # find the maximum value's key in the dict
            max_ = max(obj[i], key=obj[i].get)
            # get the positional text given as parameter as the key for the
            # highest prediction
            highest[self.data["text"][i]] = max_ if float(obj[i][max_] * 100) > 1 else "NONE"

            # prints the dict
            if show:
                print(f"'{self.data['text'][i]}'")
                print("-----------------------------")
                for key, value in obj[i].items():
                    print(f"{key} : {round(float(value) * 100, 2)}%")
                print("")
        return highest

    '''
    Helper method to get predictions from the API
    :arg  
        response : A requests object or a requests json object
    :return : a json object / dict
    '''
    @staticmethod
    def get_predictions(response):
        if response is None:
            print("[ERR] Empty object at get_predictions()")
            return
        try:
            return response["predictions"]
        except TypeError:
            return response.json()["predictions"]
        except Exception as e:
            print("Error : ", e)
            return

    # prints the http codes definition
    @staticmethod
    def http_code(response):
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
