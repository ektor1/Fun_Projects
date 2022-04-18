import requests
from urllib.parse import quote_plus as parser
import json

base_url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles="
query = "Aphrodite"

# Assign url to varible: url
url = base_url + parser(query)
print("query link: ", url)

# Package the request, send the request and catch the response: r
r = requests.get(url)
print(r)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the wiki page extract
wiki_extract = json_data['query']['pages']['1174']['extract']
print(wiki_extract)

# Save the json file
with open("Aphrodite.json", "w+") as json_file:
    json_string = json.dumps(json_data, sort_keys=True, indent=4)
    json_file.write(json_string)