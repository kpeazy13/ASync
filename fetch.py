import requests
from pathlib import Path




def fetch_ics(url):
    response = requests.get(url)
    return response.text


