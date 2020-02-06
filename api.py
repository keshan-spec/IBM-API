import requests


# 1) If parameter like this, use the create param method (RECOMMENDED)
# PARAMS = ["In hindsight, I do apologize for my previous statement.", "FUCK YOU"]

# 2) default parameter type, enclosed in single quotes with escaped strings
# PARAMS = '{"text": ["In hindsight, I do apologize for my previous statement.", "FUCK YOU"]}'

# 3) If parameter has apostrophe's or any quotation, use an escape string
# PARAMS = '{\"text\": [\"In hindsight, I do apologize for my previous statement.\", \"FUCK YOU\" ]}'


class API:
    # DEFAULT HEADER TYPE FOR APIs
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    def __init__(self, url):
        self.url = url

    '''
    Send post request to url with data and headers
    :arg 
        data : a data string formatted correctly to suit the APIs requirement (USE create_param method)
        headers : a dict of headers (Default none)
    :return : a requests object 
    '''
    def post(self, data, headers=None):
        response = requests.post(self.url, headers=headers, data=data)
        print(f"Status code : {self.http_code(response.status_code)}")
        return requests.post(self.url, headers=headers, data=data)

    '''
    Send get request to url with params and headers
    :arg 
        params : a data string formatted correctly to suit the APIs requirement (USE create_param method)
        headers : a dict of headers (Default none)
    :return : a requests object 
    '''
    def get(self, params, headers=None):
        response = requests.get(self.url, headers=headers, params=params)
        print(f"Status code : {self.http_code(response.status_code)}")
        return response

    '''
    Helper method to create parameters
    :arg  
        param : A list of string
    :return : string 
    '''
    @staticmethod
    def create_param(param):
        data = {"text": []}
        for i in param:
            data["text"].append(i.replace("'", ""))
        data = str(data).replace("'", '"')
        return data

    '''
    Helper method to get predictions from the API
    :arg  
        response : A requests object or a requests json object
    :return : a json object / dict
    '''
    @staticmethod
    def get_prediction(response):
        try:
            return response["predictions"]
        except TypeError as e:
            return response.json()["predictions"]
        except KeyError as e:
            print("Error : ", e)
            pass

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
