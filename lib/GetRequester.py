import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends the request to the URL and gets the response
        response = requests.get(self.url)
        return json.dumps(response.text)

    def load_json(self):
        # Converts response from 'get_response_body()' to JSON format
        data = self.get_response_body()
        return json.loads(data)


results = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(results.get_response_body()) 