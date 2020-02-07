# IBM API Script

This is a basic script that uses the IBM API's to detect Toxicity and Sentiment.
This can be  used for possible oter API's as well. Please refer the _api.py_ to have a better
understanding.


## api.py 
This is the main file. It contains the API Class with useful custom methods such as `get_highest_prediction(params)` and
`create_param(param)`
and some other methods. However, they aren't fully feasible for all API's.


## Usage

Usage is very simple with basic python knowledge. There are starter codes for both API's `comment_detection.py` and `sentiment_detection.py`. The predictions are returned as a _`python dict`_. 

Refer the IBM repositories:
[comments-classifier](https://github.com/IBM/MAX-Toxic-Comment-Classifier) &
[sentiment-classifier](https://github.com/IBM/MAX-Text-Sentiment-Classifier)

## Requirements
```
pip install -r requirements.txt
```

