import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends the request to the URL and gets the response
        response = requests.get(self.url)
        return response

    def load_json(self):
        # Converts response from 'get_response_body()' to JSON format
        data = self.get_response_body().json()
        return data


results = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json").load_json()
print(json.dumps(results, indent=4))