# -*- coding: utf-8 -*-
import requests
import pandas as pd

# format request
payload = {
    'data': "https://en.wikipedia.org/wiki/Manhattan_Project"
}

# target location
address = "http://127.0.0.1"
port    = '5000'

# TODO: mock endpoints
if __name__ == "__main__":
    # send request
    r = requests.get(f'{address}:{port}/wiki-entities', params=payload)
    output = r.json()['response_data']

    save_path = "/Users/mikelawrence/Documents/GitHub/RESTful-wikient/example_response.csv"
    # save data to spreadsheet
    df = pd.DataFrame(output)
    df.to_csv(save_path)

