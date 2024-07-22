# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    print("getting request")
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
        params = params.rstrip("&")  # Remove trailing '&'

    request_url = backend_url+endpoint

    if params:
        request_url = request_url+"?"+params
    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url = f"{request_url}?{params}"

    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        print("trying!")
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        # If any error occurs, print the exception details
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")  # Inspect response content
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"/analyze/"+text
    print('attempting to analyze review sentiments')
    print(request_url)
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
