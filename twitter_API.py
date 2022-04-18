import requests
import json
from decouple import config 

bearer_token = config('BEARER_TOKEN')

query = "Ukraine"
max_results = 10

# Prepare the headers to pass the authentication to Twitter's api
headers = {
    'Authorization': 'Bearer {}'.format(bearer_token),
}

params = (
    ('query', query),
    ('max_results', str(int(max_results))), # Let's make sure that the number is an string
)

# Does the request to get the most recent tweets
response = requests.get('https://api.twitter.com/2/tweets/search/recent', headers=headers, params=params)

# Validates that the query was successful
if response.status_code == 200:
    print("URL of query:", response.url)
    
    # Let's convert the query result to a dictionary that we can save as a json file
    tweets =  json.loads(response.text)
    
    # Save the json file
    with open("twitterQuery.json", "w+") as json_file:
        json_string = json.dumps(tweets, sort_keys=True, indent=4)
        json_file.write(json_string)